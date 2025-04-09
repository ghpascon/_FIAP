from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.auth.jwt import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse, RegisterUser
from app.auth.dependencies import SECRET_KEY, pwd_context
from app.database.session import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    try:
        db = get_db()
        user = db.query(User).filter_by(username=username).first()
        if user is None:
            return False

        if not verify_password(password, user.password): 
            return False

        return {"username": username}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao autenticar usuário: {str(e)}"
        )

def login(data: LoginRequest):
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    token = create_access_token({"sub": user["username"]})
    return TokenResponse(access_token=token)

def register(data: RegisterUser):
    if data.secret_key != SECRET_KEY:
        return "secret_key inválida"
    new_user = User(
        username=data.username,
        password=pwd_context.hash(data.password),
    )
    try:
        db = get_db()
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "message": "Usuário criado com sucesso.",
            "user": {
                "id": new_user.id,
                "username": new_user.username
            }
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar usuário: {str(e)}"
        )
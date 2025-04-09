from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest, TokenResponse, UserResponse
from app.auth.auth import login, register
from app.auth.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import RegisterUser


router = APIRouter(prefix="/auth", tags=["AUTH"])

@router.post(
    "/register",
    summary="Registra um novo usuário",
)
def register_route(data: RegisterUser):
    return register(data)

@router.post(
    "/login",
    summary="Realiza o Login de usuário",
)
def login_route(form_data: OAuth2PasswordRequestForm = Depends()):
    return login(form_data)

@router.get(
    "/me",
    summary="Obtem o usuário logado",
)
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}
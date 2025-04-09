from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    user:str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterUser(BaseModel):
    username: str
    password: str
    secret_key: str
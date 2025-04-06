from pydantic import BaseModel, EmailStr

data = {
    'username':'Gabriel',
    "email":"gh.pascon@gmail.com",
    "age":22,
    'is_active':False
}

class UserModel(BaseModel):
    username: str
    email: EmailStr 
    age: int
    is_active: bool

try:
    user = UserModel(**data)  
    print(user)  
except Exception as e:
    print(f"Erro na validação: {e}")
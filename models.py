from pydantic import BaseModel

class UserLogin(BaseModel):
    login: str
    password: str

class AuthResp(BaseModel):
    res: int
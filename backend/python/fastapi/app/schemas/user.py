from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    role: str
    password: str

class UserOut(BaseModel):
    idUser: int
    name: str
    role: str
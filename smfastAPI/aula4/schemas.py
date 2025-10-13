from pydantic import BaseModel

class UsuariIn(BaseModel):
    nome: str
    email: str
    idade: int

class UsuariOut(BaseModel):
    id: int
    nome: str
    email: str
    idade: int

    class Config:
        orm_mode = True
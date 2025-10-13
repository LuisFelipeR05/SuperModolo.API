from fastapi import FastAPI, Response
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    email: str
    passowrd: str

class UserOut(BaseModel):
    username: str
    email: str


list_users = []

app = FastAPI(title="API de cadastro de usuários")

@app.get("/users")
def get_all_users()-> list[UserOut]:
    return list_users

@app.post("/users")
def add_new_user(user:UserIn) ->UserOut:
    list_users.append(user)
     # return Response(content="Usuário adicionado com sucesso!")
    return user



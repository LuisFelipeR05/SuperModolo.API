from fastapi import FastAPI,Response,HTTPException
from pydantic import BaseModel


app = FastAPI()

class userIn(BaseModel):
    username: str
    email: str

users = []

app = FastAPI(title="cadastr de usuario")

@app.post("/users/")
async def add_new_user(user: userIn):
    users.append(user.model_dump())
    print(users)
    return Response("usuário adicionado com, sucesso!",status_code=201)

@app.get("/users")
async def get_all_users():
    if len(users) == 0:
        return Response(status_code=204,content="sem conteudo")
    print("ola mundo")
 
    return users


@app.put("/users/")
async def update_user(user: userIn):
    for u in users:
        if u["username"] == user.username:
            u["email"] = user.email
            return Response("usuário atualizado com sucesso!",status_code=200)
    raise HTTPException(status_code=404,detail="usuário não encontrado")
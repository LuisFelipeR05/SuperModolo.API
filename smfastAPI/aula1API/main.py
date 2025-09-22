from fastapi import FastAPI,HTTPException,Response


app = FastAPI()

users_list = []


@app.post("/users/{nome}")
async def add_new_user(nome:str):
    users_list.append(nome)
    return Response(
        "usuario adicionado com sucesso",
        status_code=201
        )

@app.get("/users/{id}")
async def get_user_by_id(id:int):
    try :
        return users_list[id]
    except:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.put("/users")
async def atualizar_usuario():
    pass

        

@app.get("/users",status_code=200)
async def get_all_users():
    if len (users_list) == 0:
        return Response(
            "not content",
            status_code=204
        )   

    return users_list

@app.delete("/users/{nome}")
async def deletar_usuario(nome:str):
    if nome not in users_list:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    users_list.remove(nome)
    return Response(
        "usuario removido com sucesso",
        status_code=200
    )
from ast import stmt
from fastapi import FastAPI,Depends
from schemas import UsuarioIn,UsuarioOut
from DB import UsuarioDB,pegar_session,session,query
from sqlalchemy.orm import Session

query()

app = FastAPI()

@app.post("/usuario")
async def adicionar_novo_usuario(
    Usuario:UsuarioIn,
    db:Session=Depends(pegar_session)
    ):
    Usuario_db = UsuarioDB(
        nome=Usuario.nome,
        email=Usuario.email,
        idade=Usuario.idade
    )

    db.add(Usuario_db)
    db.commit()
    db.refresh(Usuario_db)
    return Usuario_db

@app.get("/user")
async def pegar_todos_os_usuarios(db:Session=Depends(pegar_session)) -> list[UsuarioOut]:
    stmt = db.query(UsuarioDB).all()
    return stmt

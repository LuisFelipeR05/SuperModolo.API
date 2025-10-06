from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel

estoque = []

class ProductsIn(BaseModel):
    id:int = None
    name: str
    price: float
    amount: int

class ProductOut(BaseModel):
    id:int
    name: str
    price: float



app = FastAPI (title="Cadastro de Produtos!")


@app.get("/products")
async def get_products_by_id(id:int):
    try:
        return estoque[id]
    except:
        raise HTTPException(status_code=404, detail= "Produto não Encontado")
    
@app.post("/products")
async def add_new_products():
    estoque.append(estoque)

    return Response(
        "Produto Cadastrado com Sucesso!",
        status_code=201
    )

@app.put("/products")
async def update_product(product: ProductsIn,id:int):
        estoque[id] = product
        return Response("Produto Atualizado com Sucesso!")
        raise HTTPException(status_code=404,detail="Produto Não Encontrado!")


@app.delete("/products/{id}")
async def delete_product(id:int):
    if id not in estoque:
        raise HTTPException(status_code=404,detail="Produto Não Encontrado")
    estoque.remove(id)
    return Response(
        "Produto Removido com Sucesso!",
        status_code=200
    )
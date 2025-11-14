from fastapi import FastAPI
import funcao

app = FastAPI(title="Almoxarifado da loja")

@app.get("/")
def home():
    return {"Mensagem": "Bem vindo ao estoque de produtos da loja"}


# - Cadastro de items

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco_unitario: float, quantidade: int):
    funcao.cadastrar_produto(nome, categoria, preco_unitario, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso"}
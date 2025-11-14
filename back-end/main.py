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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produto()
    lista = []


    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })

    return {"produtos": lista}



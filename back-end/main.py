from fastapi import FastAPI
import funcao

app = FastAPI(title="Almoxarifado da loja")

@app.get("/")
def home():
    return {"Mensagem": "Bem vindo ao esoque de produtos da loja"}
import streamlit as st
import requests



API_URL = "http://127.0.0.1:8000"


st.set_page_config(page_title= "Produtos", layout="wide")
st.title("Estoque de produtos")

menu = st.sidebar.radio("menu",
["Adicionar produto", "Ver os produtos", "Atualizar produtos", "Excluir produto" ]
)
if menu == "Ver os produtos":
    st.header("📦Estoque")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.write("Nenhum produto cadastrado. ")
    else:
        st.write("Não foi exibir os produtos ")

elif menu == "Adicionar produto":
    st.header("➕ Adicionar Novo Produto")
  
    nome = st.text_input("nome")
    categoria = st.text_input("Categoria")
    preco = st.number_input("preco", min_value=0.0, step=0.5)
    quantidade = st.number_input("quantidade", min_value=1, max_value=100, step=1)
    if st.button("Adicionar produto"):
        if nome and categoria:
            params = {
                "nome": nome,
                "categoria": categoria,
                "preco_unitario": preco,
                "quantidade": quantidade,            
            }
            
            response= requests.post(f"{API_URL}/produtos", params=params)

            if response.status_code == 200:
                st.success("Produto cadastrado com sucesso")
            else:
                st.error("Erro ao cadastrar produto")
        else:
            st.warning("Preencha todos os campos obrigatórios")



elif menu == "Atualizar produtos":
    st.header(" 🔃 Atualizar produtos")
    id_produto = st.number_input("id do produto a ser atualizado", min_value=1, step=1)
    preco = st.number_input("Novo preco", min_value=0.0, step=0.5)
    quantidade = st.number_input("Nova quantidade", min_value=1, max_value=100, step=1)
    if st.button("atualizar"):
        dados = {
            "id": id_produto,
            "novo_preco": preco,
            "nova_quantidade": quantidade
        }
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto atualizado coom sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atualizar produto.")









        
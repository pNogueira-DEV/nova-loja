import streamlit as st
import requests



API_URL = "http://127.0.0.1:8000/"


st.set_page_config(page_title= "Filmes", layout="wide")
st.title("Estoque de produtos")

menu = st.sidebar.radio("menu",
                        ["Adicionar produto", "Ver os produtos", "Atualizar produtos", "Excluir produto" ]
                        )
if menu == "Ver os produtos":
    st.subheader = ("Produts Disponíveis abaixo ⬇")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.write("Nenhum produto cadastrado. ")
    else:
        st.write("Não foi exibir os produtos ")



        
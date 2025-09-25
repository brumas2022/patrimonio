import streamlit as st
from funcao_contratos import inserir1

st.set_page_config("Modulo para inserir dados", layout="wide")


st.sidebar.button("INSERIR", on_click=inserir1)
#inserir()

st.sidebar.button("MOSTRAR")

st.sidebar.button("ATUALIZAR")


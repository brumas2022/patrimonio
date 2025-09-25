import streamlit as st
from funcao_contratos import inserir

st.set_page_config("Modulo para inserir dados", layout="wide")


if st.sidebar.button("INSERIR"):
    inserir()

st.sidebar.button("MOSTRAR")

st.sidebar.button("ATUALIZAR")


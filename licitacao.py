import streamlit as st
import pandas as pd

st.set_page_config("Licitações de materiais", layout="wide")

def inserir():
    st.write("Este é o modulo de inserção")

def consulta():
    st.write("Este é o modulo de consulta")
  
i=st.sidebar.button("INSERIR")
c=st.sidebar.button("CONSULTAR")

if i:
   inserir()

if c:
   consulta()



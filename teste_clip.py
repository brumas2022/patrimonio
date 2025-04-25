import streamlit as st
import pandas as pd


botao = st.button("Aperte aqui")
if botao:
   teste = pd.read_clipboard(sep=",", names=["Nome", "Cargo", "Tipo"])
   st.write(teste)

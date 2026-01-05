import pandas as pd
import streamlit as st

tabela = pd.read_excel("controle_analise.xlsx", sheet_name=0)

st.dataframe(tabela)
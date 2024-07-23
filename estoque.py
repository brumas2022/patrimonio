import streamlit as st
import pandas as pd 

st.set_page_config("Consulta estoque", layout="wide")

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=1)

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME"))

if consulta=="POR ITEM":
   st.write("Consulta por item")
   st.dataframe(df)
elif consulta=="POR NOME":
   st.write("Consulta por nome")



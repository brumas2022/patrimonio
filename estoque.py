import streamlit as st
import pandas as pd 

st.set_page_config("Consulta estoque", layout="wide")

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=0)

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME"))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   df.columns=['Item', 'Descrição', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   df.set_index("Item", inplace=True)
   
   st.dataframe(df.iloc[3:])
   #selecao = df['Item']=="1974"
   #line = df.loc[df["Item"] == '1974']
   #st.dataframe(line)

elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")



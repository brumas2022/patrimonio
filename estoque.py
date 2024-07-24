import streamlit as st
import pandas as pd 
import openpyxl

st.set_page_config("Consulta estoque", layout="wide")

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME"))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   item = df['Item'].tolist()
   b = st.selectbox("Escolha o item", item)
   resultado_item = df[df['Item']==b]
   st.dataframe(resultado_item)
   
   #df.set_index("Item", inplace=True)
   st.dataframe(df.iloc[3:])
   valor = 19
 
   resultado = df[df['Item'] == valor]
   st.dataframe(df.iloc[valor])
   
   
   #selecao = df['Item']=="1974"
   #line = df.loc[df["Item"] == '1974']
   #st.dataframe(line)

elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")
   nomes = df['Descricao'].tolist()
   a = st.selectbox("Escolha a descrição :", nomes)

   resultado = df[df['Descricao']==a]
   st.dataframe(resultado)



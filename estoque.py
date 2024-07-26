import streamlit as st
import pandas as pd 
import openpyxl

st.set_page_config("Consulta estoque", layout="wide")
st.image("logosanear.png")

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=2)
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME", "TODOS"))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   item = df['Item'].tolist()
   b = st.selectbox("Escolha o item", item, index=None, placeholder="Digite o nro...")
   resultado_item = df[df['Item']==b]
   st.dataframe(resultado_item, hide_index=True)
   #st.write(resultado_item.iat[1,1])
   
   #df.set_index("Item", inplace=True)
         
elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")
   nomes = df['Descricao'].tolist()
   a = st.selectbox("Escolha a descrição :", nomes, index=None, placeholder="Digite o nome....")

   resultado = df[df['Descricao']==a]
   st.dataframe(resultado, hide_index=True)
   
elif consulta=="TODOS":
   st.dataframe(df.iloc[3:], hide_index=True)
   



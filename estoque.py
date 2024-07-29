import streamlit as st
import pandas as pd 
import openpyxl

st.set_page_config("Consulta estoque", layout="wide")
st.image("logosanear.png")

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=3)
df1=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=3)  ##para testes
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME", "TODOS"))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   item = df['Item'].tolist()
   b = st.selectbox("Escolha o item", item, index=None, placeholder="Digite o nro...")
   resultado_item = df[df['Item']==b]
   st.dataframe(resultado_item, hide_index=True)

   
   #nome=df.columns[2]
   st.write("Data e horario da atualização : ", df1.columns[1])

   #st.write(resultado_item.iat[1,1])
   
   #df.set_index("Item", inplace=True)
         
elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")
   nomes = df['Descricao'].tolist()
   a = st.selectbox("Escolha a descrição :", nomes, index=None, placeholder="Digite o nome....")

   resultado = df[df['Descricao']==a]
   st.dataframe(resultado, hide_index=True)
   st.write("Data e horario da atualização : ", df1.columns[1])
   
elif consulta=="TODOS":
   st.write("Data e horario da atualização : ", df1.columns[1])
   st.dataframe(df.iloc[3:], hide_index=True)
   
   



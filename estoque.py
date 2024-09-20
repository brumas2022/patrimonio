import streamlit as st
import pandas as pd 
import openpyxl
#from fpdf import FPDF
from openpyxl import load_workbook
import webbrowser
import datetime


st.set_page_config("Consulta estoque SANEAR", layout="wide")
colimage = st.columns((1,1,1))
colimage[1].image("logosanear.png", width=300)

def estoque_zero():
   st.info("As informações desta seção refere-se ao banco de dados da Coplan com todos os itens zerados no estoque")
   df_zero=pd.read_excel("estoque-zero.xlsx", sheet_name=28)
   df_zero.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   item_zero=df_zero["Item"].tolist()
   z = st.selectbox("Escolhao item", item_zero)
   resultado_item_zero=df_zero[df_zero["Item"]==z]
   st.dataframe(resultado_item_zero, hide_index=True)
   st.write("Data e horario da atualização : ", df_zero.columns[1])   

def nad():
   st.header("Controle das NADS")
   st.info("Acompanhe o andamento das NADS aqui")
   df_nad=pd.read_excel("controle_nad.xlsx", sheet_name=0)
   df_new=df_nad.style.format(precision=0, thousands=".", decimal=",")
   
   st.dataframe(df_nad.style.set_properties(**{'color':'blue', 'background-color':'yellow'}))
   st.dataframe(df_new)
   df_nad1=pd.read_excel("controle_nad.xlsx", sheet_name=1)
   
   # teste com tabela editavel
   #data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
   #     'Idade': [25, 31, 42, 28],
   #     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']}
   #dft = pd.DataFrame(data)
   # Criar um widget de tabela para exibir o DataFrame
   #st.data_editor(dft)
   
# INICIO DO PROGRAMA 
# Transforma tabela do excel em DataFrame
df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=42)
data_atualizacao = df.columns[1]

st.write("Atualizado em :", data_atualizacao)

df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
lista_consulta=["POR ITEM", "POR NOME", "TODOS", "ESTOQUE-ZERO", "NAD"]

hoje = datetime.date.today() 
st.write("A data atual é : ", hoje.strftime("%d/%m/%Y"))

consulta = st.selectbox("Escolha o tipo de consulta", (lista_consulta))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   st.info("Nesta seção você precisa saber o numero do item a ser pesquisado")
   item = df['Item'].tolist()
   b = st.selectbox("Escolha o item", item, index=None, placeholder="Digite o nro...")
   resultado_item = df[df['Item']==b]
   st.dataframe(resultado_item, hide_index=True)

        
         
elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")
   st.info("Nesta seção você pode pesquisa pelo nome do item")
   nomes = df['Descricao'].tolist()
   a = st.selectbox("Escolha a descrição :", nomes, index=None, placeholder="Digite o nome....")

   resultado = df[df['Descricao']==a]
   
   st.dataframe(resultado, hide_index=True)
   
   
elif consulta=="TODOS":
   st.dataframe(df.iloc[3:], hide_index=True)

   
elif consulta=="ESTOQUE-ZERO":
   estoque_zero()
   

elif consulta=="NAD":
   nad() 
      
         
   
   
   



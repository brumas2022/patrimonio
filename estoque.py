import streamlit as st
import pandas as pd 
import openpyxl
#from fpdf import FPDF
from openpyxl import load_workbook
import webbrowser


st.set_page_config("Consulta estoque SANEAR", layout="wide")
colimage = st.columns((1,1,1))
colimage[1].image("logosanear.png", width=300)

def controle():
   a=st.sidebar.button("Agua")
   b=st.sidebar.button("Esgoto")
   c=st.sidebar.button("Residuos")
   d=st.sidebar.button("Aguas pluviais")
   if a:
      tab1, tab2, tab3, tab4 = st.tabs(["Tabela 1", "Tabela 2", "Tabela 3", "Tabela 4"])
   if b:
      tab1, tab2, tab3, tab4 = st.tabs(["Tabela 1", "Tabela 2", "Tabela 3", "Tabela 4"])
   if c:
      tab1, tab2, tab3, tab4 = st.tabs(["Tabela 1", "Tabela 2", "Tabela 3", "Tabela 4"])
   if d:
      tab1, tab2, tab3, tab4 = st.tabs(["Tabela 1", "Tabela 2", "Tabela 3", "Tabela 4"])
def imprimir():
   #st.page_link("https://gmail.com")
   #df_orc.to_excel("orcamento.xlsx", index=False)
   st.write("funcionou")
   #pdf = FPDF()
   #pdf.add_page()
   #pdf.set_font("Arial")
   #pdf.text(115, 145, "Orçamento")
   #pdf.output('orcamento.pdf')

def estoque_zero():
   st.info("As informações desta seção refere-se ao banco de dados da Coplan com todos os itens zerados no estoque")
   df_zero=pd.read_excel("estoque-zero.xlsx", sheet_name=25)
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
   st.dataframe(df_nad.style.set_properties(**{'color':'blue', 'background-color':'yellow'}))
   df_nad1=pd.read_excel("controle_nad.xlsx", sheet_name=1)
   
   
   data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
        'Idade': [25, 31, 42, 28],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']}
   dft = pd.DataFrame(data)
   # Criar um widget de tabela para exibir o DataFrame
   st.data_editor(dft)
   

df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=39)
data_atualizacao = df.columns[1]
df1=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=39)  ##para testes
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
lista_consulta=["POR ITEM", "POR NOME", "TODOS", "ESTOQUE-ZERO", "NAD"]

data_atualizacao.dtype

consulta = st.selectbox("Escolha o tipo de consulta", (lista_consulta))

if consulta=="POR ITEM":
   st.write("Consulta por ordem numerica")
   st.info("Nesta seção você precisa saber o numero do item a ser pesquisado")
   item = df['Item'].tolist()
   b = st.selectbox("Escolha o item", item, index=None, placeholder="Digite o nro...")
   resultado_item = df[df['Item']==b]
   st.dataframe(resultado_item, hide_index=True)

   
   #nome=df.columns[2]
   st.write("Data e horario da atualização : ", data_atualizacao)

   #st.write(resultado_item.iat[1,1])
   
   #df.set_index("Item", inplace=True)
   
         
elif consulta=="POR NOME":
   st.write("Consulta por ordem alfabetica")
   st.info("Nesta seção você pode pesquisa pelo nome do item")
   nomes = df['Descricao'].tolist()
   a = st.selectbox("Escolha a descrição :", nomes, index=None, placeholder="Digite o nome....")

   resultado = df[df['Descricao']==a]
   
   st.dataframe(resultado, hide_index=True)
   st.write("Data e horario da atualização : ", df1.columns[1])
   
elif consulta=="TODOS":
   st.write("Data e horario da atualização : ", df1.columns[1])
   st.dataframe(df.iloc[3:], hide_index=True)

   
elif consulta=="ESTOQUE-ZERO":
   estoque_zero()
   #controle()

elif consulta=="NAD":
   nad() 
      
         
   
   
   



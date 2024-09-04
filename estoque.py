import streamlit as st
import pandas as pd 
import openpyxl
#from fpdf import FPDF
from openpyxl import load_workbook
import webbrowser

st.set_page_config("Consulta estoque SANEAR", layout="wide")
st.image("logosanear.png")

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
   #st.markdown("Em construção")
   df_zero=pd.read_excel("estoque-zero.xlsx", sheet_name=16)
   df_zero.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   item_zero=df_zero["Item"].tolist()
   z = st.selectbox("Escolhao item", item_zero)
   resultado_item_zero=df_zero[df_zero["Item"]==z]
   st.dataframe(resultado_item_zero, hide_index=True)
   st.write("Data e horario da atualização : ", df_zero.columns[1])   

def nad():
   st.header("Controle das NADS")
   df_nad=pd.read_excel("controle_nad.xlsx", sheet_name=0)
   #df_nad.map(neg_vermelho)
   df_nad.style.highlight_null(color='red')
   st.dataframe(df_nad)

def neg_vermelho(val):
   color='red' if val < 1000 else 'black'   
   return 'color : {0!s}'.format(color)


df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=30)
df1=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=30)  ##para testes
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
lista_consulta=["POR ITEM", "POR NOME", "TODOS", "ESTOQUE-ZERO", "NAD"]

consulta = st.selectbox("Escolha o tipo de consulta", (lista_consulta))

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

elif consulta=="ORÇAMENTO":
   st.write("Escolha os produtos")
   lista_orc=[]
   qtdes=[]
   nomes_orc = df['Descricao'].tolist()
   col=st.columns([1,1,1])
  
   # INSERIR OS PRODUTOS DO ESTOQUE PARA AQUISICAO
   
   item_orc1=col[0].selectbox("Descrição 1", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde1=col[1].text_input("Qtde produto 1 : ")
   
   item_orc2=col[0].selectbox("Descrição 2 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde2=col[1].text_input("Qtde produto 2 : ")
   
   item_orc3=col[0].selectbox("Descrição 3 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde3=col[1].text_input("Qtde produto 3 : ")

   # CRIAR AS LISTAS 
   lista_orc.append(item_orc1)
   lista_orc.append(item_orc2)
   lista_orc.append(item_orc3)
   qtdes.append(qtde1)
   qtdes.append(qtde2)
   qtdes.append(qtde3)

   # MOSTRAR NA TELA OS ITENS ESCOLHIDOS
   lista_total=list(zip(lista_orc, qtdes))
   df_orc=pd.DataFrame(lista_total, columns=['Descricao', 'Qtde'])
                       
   col[0].dataframe(df_orc, use_container_width=True)
   #df_orc.to_excel("orcamento.xlsx", index=False)
   #col[1].dataframe(qtdes)
   df_orc.to_excel("orcamento.xlsx", sheet_name='Planilha1')

   

   # DISPARAR PARA FORNECEDORES
   enviar = col[0].button("ENVIAR POR EMAIL PARA FORNECEDORES", on_click=imprimir)
   #enviar = col[0].button("ENVIAR POR EMAIL PARA FORNECEDORES")
   #col[0].link_button("ENVIAR ORCAMENTO", "https://mail.google.com/mail/u/0/#inbox?compose=new")
   #col[0].link_button("ENVIAR ORCAMENTO", "https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSKkHdPzwgWkcrNGPSHrrKdTGvlGShJwtqqrtkpppgzfSbRtqKjbKXrwzFCvbNDLrMzCrWhP")
   #from openpyxl.workbook import Workbook
   #writer = pd.ExcelWriter("/mount/src/patrimonio/amostra.xlsx")
   #df_orc.to_excel(writer, sheet_name='Planilha1')
   #writer._save()
   
elif consulta=="ESTOQUE-ZERO":
   estoque_zero()
   #controle()

elif consulta=="NAD":
   nad() 
      
         
   
   
   



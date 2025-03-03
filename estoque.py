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

def entrar():
   usuario=st.text_input("Digite seu nome")
   senha=st.text_input("Digite sua senha")
   go=st.button("GO")
   if go:   
      pass
         
      

def medicao():
   #st.header("Controle do PREGAO 013/2024")
   st.info("CAPTAÇÃO DE AGUA BRUTA, ELEVATORIA RC1, ELEVATORIA RC2 E UFMT")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=0)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA EMVIO NAD", "SITUACAO", "PRAZO DE ENTREGA", "DIAS", "OBSERVACAO"]
   
   ##"LOTE", "EMPRESA", "VALOR", "DATA EMVIO NAD", "SITUACAO", "PRAZO DE ENTREGA", "DIAS", "OBSERVACAO"
   st.dataframe(df_medicao.iloc[3:16], hide_index=True)
   
def medicao1():
   #st.header("Controle do PREGAO 014/2024")
   st.info("LOTEAMENTOS CPA, MARIA AMELIA, ALTAMIRANDO II E ALFREDO III")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=1)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2"]
   
   
   st.dataframe(df_medicao.iloc[3:16], hide_index=True)
     
def medicao2():
   #st.header("Controle do PREGAO 014/2024")
   st.info("AMPLIAÇÃO DO SISTEMA DE ABASTECIMETNO DE ÁGUA NA ESTAÇÃO DE TRATAMENTO DE ÁGUA (ETA)")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=2)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2"]
   
   #st.dataframe(df_medicao, hide_index=True, column_config={
   #     "DATA NAD1": st.column_config.DatetimeColumn(
   #         "DATA NAD1",
   #         format="D MM YYYY",
   #         
   #     ),
   # })
   
   
   st.dataframe(df_medicao.iloc[3:8], hide_index=True)
   with open("PREGAO 13.xlsx", "rb") as file: 
      st.download_button(label='PLANILHA ORIGINAL', data=file, file_name="PREGAO 13.xlsx") 
      
         
def estoque_zero():
   ##entrar()
   st.info("As informações desta seção refere-se ao banco de dados da Coplan com todos os itens zerados no estoque")
   df_zero=pd.read_excel("Zero_Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
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
   #dfnovo=df_nad.style.apply(highlight, axis=1)
   
   def highlight_survived(s):
    return ['background-color: darkorange']*len(s) if s['entrega total'] == 'ok' else ['background-color: lightgrey']*len(s)

   
   
   df_new=df_nad.style.format(precision=0, thousands=".", decimal=",").apply(highlight_survived, axis=1)
   ##.highlight_between(subset='entrega total', left="ok", color="red")
   #.format(subset="entrega prevista", na_rep="MISS").set_table_styles9[{'selector':'tr:hover', 'props':[('background-color', 'black'), ('color', 'white')]}]
   #.highlight_between(subset='entrega total', left="ok", color="red")
   #st.dataframe(df_nad.style.set_properties(**{'color':'blue', 'background-color':'yellow'}), hide_index=True)
   
   
   st.dataframe(df_new, hide_index=True, column_config={
        "data envio": st.column_config.DatetimeColumn(
            "data envio",
            format="D MMM YYYY, h:mm a",
            
        ),
    })
   #dfteste=pd.read_excel("controle_nad.xlsx", sheet_name=0)
   #dfnovo=dfteste.style.apply(lambda _: "background-color: green", subset=(dfteste.index[1],))
   #st.dataframe(dfnovo)
   
   
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
df=pd.read_excel("Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
data_atualizacao = df.columns[1]

st.write("Atualizado em :", data_atualizacao)

df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
lista_consulta=["POR ITEM", "POR NOME", "TODOS", "ESTOQUE-ZERO", "NAD", "PREGAO 013", "PREGAO 014", "PREGAO 012"]

hoje = datetime.date.today() 
st.write("A data atual é : ", hoje.strftime("%d/%m/%Y"))

col = st.columns((1,1,1))

consulta = col[0].selectbox("Escolha o tipo de consulta", (lista_consulta))

if consulta=="POR ITEM":
   colitem = st.columns((1,1,1))
   colitem[0].write("Consulta por ordem numerica")
   colitem[0].info("Nesta seção você precisa saber o numero do item a ser pesquisado")
   item = df['Item'].tolist()
   b = colitem[0].selectbox("Escolha o item", item, index=None, placeholder="Digite o nro...", )
   resultado_item = df[df['Item']==b]
   #colitem[1].write("Nome "+resultado_item[1])
   #st.dataframe(resultado_item, hide_index=True)
   colitem[1].dataframe(resultado_item['Item'], hide_index=True, use_container_width=True)
   colitem[1].dataframe(resultado_item['Descricao'], hide_index=True, use_container_width=True)
   colitem[1].dataframe(resultado_item['Qtde'], hide_index=True, use_container_width=True)

        
         
elif consulta=="POR NOME":
   colnome = st.columns((1,1,1))
   colnome[0].write("Consulta por ordem alfabetica")
   colnome[0].info("Nesta seção você pode pesquisar pelo nome do item")
   nomes = df['Descricao'].tolist()
   a = colnome[0].selectbox("Escolha a descrição :", nomes, index=None, placeholder="Digite o nome....")

   resultado = df[df['Descricao']==a]
   
   #st.dataframe(resultado, hide_index=True)
   colnome[1].dataframe(resultado['Item'], hide_index=True, use_container_width=True)
   colnome[1].dataframe(resultado['Descricao'], hide_index=True, use_container_width=True)
   colnome[1].dataframe(resultado['Qtde'], hide_index=True, use_container_width=True)
   
   
elif consulta=="TODOS":
   form = st.form(key="Caes", clear_on_submit=True)
   with form:
      email = st.text_input("Qual o seu nome")
      a=st.text_input("Entre com a senha", type="password" )
      #b=os.getenv("senha")
      b="102030"
      botao_submit = form.form_submit_button("Confirma!")
   if a==b:
      st.write("{email} Vc acertou!!!")
      st.dataframe(df.iloc[3:], hide_index=True)

   
elif consulta=="ESTOQUE-ZERO":
   estoque_zero()
   

elif consulta=="NAD":
   nad() 
      
elif consulta=="PREGAO 013":
   ##st.write("EM CONSTRUÇÃO")
   medicao()

elif consulta=="PREGAO 014":
   medicao1()        

elif consulta=="PREGAO 012":
   medicao2()
   
   



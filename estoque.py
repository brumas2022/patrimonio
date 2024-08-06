import streamlit as st
import pandas as pd 
import openpyxl
from fpdf import FPDF

st.set_page_config("Consulta estoque SANEAR", layout="wide")
st.image("logosanear.png")


df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=9)
df1=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=9)  ##para testes
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME", "TODOS", "ORÇAMENTO"))

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
   item_orc1=col[0].selectbox("Escolha produto 01 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde1=col[1].text_input("Qtde produto 1 : ")
   
   item_orc2=col[0].selectbox("Escolha produto 02 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde2=col[1].text_input("Qtde produto 2 : ")
   
   item_orc3=col[0].selectbox("Escolha produto 03 :", nomes_orc, index=None, placeholder="Digite o nome....")
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
                       
   col[0].dataframe(df_orc)
   #col[1].dataframe(qtdes)

   

   # DISPARAR PARA FORNECEDORES
   enviar = col[0].button("ENVIAR POR EMAIL PARA FORNECEDORES")
   if enviar:
      df_orc.to_excel('orcamento.xlsx', index=False)

      st.write(orcamento.xlsx)
      #pdf = FPDF()
      #pdf.add_page()
      #pdf.set_font("Arial")
      #pdf.text(115, 145, "Orçamento")
      #pdf.output('orcamento.pdf', 'D')
      
         
   
   
   



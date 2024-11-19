import pandas as pd
import streamlit as st

global qtde1

def lista_numero():
    global df
    df=pd.read_excel("Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
    df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
    nomes_orc = df['Item'].tolist()
    return nomes_orc

col = st.columns([0.25, 0.5, 0.25])
col[0].write("Numero do produto")
col[1].write("Descrição do produto")
col[2].write("Quantide do produto")

##qtde1 = " "
def exemplo():
    atividade = []
    while atividade:
          atividade = input("Digite uma atividade") 
    print(atividade)         


exemplo()

def teste():
    
    while qtde1==" ":
    
       item_orc1=col[0].selectbox(" ", lista_numero())
       resultado_item1 = df[df['Item']==item_orc1]

       descricao1=resultado_item1.iat[0,1]
    
       col[1].write(descricao1)
  
       qtde1=col[2].text_input(" ")
    
  


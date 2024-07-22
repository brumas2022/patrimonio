import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config("Licitações de materiais", layout="wide")

def inserir():
    st.write("Este é o modulo de inserção")
    with st.form("ENTRA", clear_on_submit=True):
         col = st.columns((1,1))
         a1 = col[0].text_input("Objeto da licitacao")
         a2 = col[0].text_input("Data inicial")
         
         enviar = st.form_submit_button("ENTRA")
def inserir1():
    try:
               connection = psycopg2.connect(
                         host='aws-0-sa-east-1.pooler.supabase.com',
                         user='postgres.hdhvkseneldllvnlvpgc',
                         password='Hoje#estamos#fortes#como#geleia',
                         database='postgres',
                         port='5432'

               )
               st.write("conexao exitosa")
               cursor = connection.cursor()
               comando = f"""INSERT INTO Patrimonio (objeto, datainicial) VALUES ('{a1}', '{a2}')"""
               cursor.execute(comando)
               connection.commit()
               st.text("Cadastro efetuado com sucesso")
               cursor.close()
               connection.close()
         
    except Exception as ex:
               st.write(ex)
        
def consulta():
    st.write("Este é o modulo de consulta")
  
i=st.sidebar.button("INSERIR")
c=st.sidebar.button("CONSULTAR")

if i:
    inserir()
    inserir1()
    
  

if c:
   consulta()



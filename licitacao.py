import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import folium


st.set_page_config("Licitações de materiais", layout="wide")

class Computador:
    def __init__(self, marca, memoria, video):
        self.marca = marca
        self.memoria = memoria
        self.video = video

def inserir():
    st.write("Este é o modulo de inserção")
    with st.form("ENTRA", clear_on_submit=True):
         col = st.columns((1,1))
         a1 = col[0].text_input("Objeto da licitacao")
         a2 = col[0].date_input("Data inicial")
         #a3 = col[0].text_input("Nro da Modalidade")
         
         enviar = st.form_submit_button("ENTRA")
def inserir1(a1,a2):
    try:
               connection = psycopg2.connect(
                         host='aws-0-sa-east-1.pooler.supabase.com',
                         user='postgres.hdhvkseneldllvnlvpgc',
                         password='Hoje#estamos#fortes#como#geleia',
                         database='postgres',
                         port='6543'

               )
               st.write("conexao exitosa")
               cursor = connection.cursor()
               comando = f"""INSERT INTO patrimonio (objeto, datainicial, modalidade) VALUES ('{a1}', '{a2}', '{a3}')"""
               cursor.execute(comando)
               connection.commit()
               st.text("Cadastro efetuado com sucesso")
               cursor.close()
               connection.close()
         
    except Exception as ex:
               st.write(ex)
        
def consulta():
    st.write("Este é o modulo de consulta")
    #engine = create_engine('postgresql://postgres.hdhvkseneldllvnlvpgc:Hoje#estamos#fortes#como#geleia@aws-0-sa-east-1.pooler.supabase.com:6543/postgres')
    try:
               connection = psycopg2.connect(
                         host='aws-0-sa-east-1.pooler.supabase.com',
                         user='postgres.hdhvkseneldllvnlvpgc',
                         password='Hoje#estamos#fortes#como#geleia',
                         database='postgres',
                         port='6543'

               )
               st.write("conexao exitosa")
               cursor = connection.cursor()
               comando = "SELECT * FROM Patrimonio"
               cursor.execute(comando)
               resultado=cursor.fetchall()
               resultado1=pd.DataFrame(resultado)
               resultado1.columns=['Id', 'Entrada', 'Licitacao', 'Data', 'Modalidade'] 
               resultado1.set_index("Id", inplace=True) 
               resultado1['Data'] = pd.to_datetime(resultado1.Data)
               resultado1['Data'] = resultado1['Data'].dt.strftime('%d/%m/%Y')
               st.dataframe(resultado1)
         
    except Exception as ex:
               st.write(ex)

col1=st.columns((1,1,1,1))

escolha=col1[0].selectbox("ESCOLHA A OPÇÃO", ("INSERIR", "CONSULTA", "CLASSE"))

if escolha=="INSERIR":
    st.write("Este é o modulo de inserção")
    with st.form("ENTRA", clear_on_submit=True):
         col = st.columns((1,1))
         a1 = col[0].text_input("Objeto da licitacao")
         a2 = col[0].text_input("Data inicial")
         a3 = col[0].text_input("Nro da Modalidade")
         enviar = st.form_submit_button("ENTRA")
    if enviar:
       inserir1(a1,a2)
        
elif escolha=="CONSULTA":
     
     consulta()

elif escolha=="CLASSE":
    computador = Computador("asus", "16GB", "N7vidia")
    st.write(computador.marca)
    from streamlit_folium import st_folium
    mapa = folium.Map(location=[-16.4507341,-54.6498371], zoom_start=17, popup='SANEAR')
    st_folium(mapa)
    #-16.4507341,-54.6498371,17z
   
  




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
def inserir1(a1,a2,a3,a4):
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
               comando = f"""INSERT INTO patrimonio (objeto, datainicial, datafinal, modalidade) VALUES ('{a1}', '{a2}', '{a3}', '{a4}')"""
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
               resultado1.columns=['Id', 'Entrada', 'Licitacao', 'Data Inicio', 'Modalidade', 'Data Final'] 
               resultado1.set_index("Id", inplace=True) 
               #resultado1['Data Inicio'] = pd.to_datetime(resultado1.Data)
               #resultado1['Data Inicio'] = resultado1['Data Inicio'].dt.strftime('%d/%m/%Y')
               #resultado1['Data Final'] = pd.to_datetime(resultado1.Data)
               #resultado1['Data Final'] = resultado1['Data Final'].dt.strftime('%d/%m/%Y')
               
               st.dataframe(resultado1)
         
    except Exception as ex:
               st.write(ex)

col1=st.columns((1,1,1,1))

lista=['INSERIR', 'CONSULTA', 'CLASSE', 'MAPA']

escolha=col1[0].selectbox("ESCOLHA A OPÇÃO", lista)

if escolha=="INSERIR":
    st.write("Este é o modulo de inserção")
    with st.expander('leia mais aqui'):
      st.write("Neste local serão inseridas as informações sobre as licitacoes")
    with st.form("ENTRA", clear_on_submit=True):
         col = st.columns((1,1))
         a1 = col[0].text_input("Objeto da licitacao")
         a2 = col[0].text_input("Data inicial")
         a3 = col[0].text_input("Data Final")
         a4 = col[0].text_input("Nro da Modalidade")
         enviar = st.form_submit_button("ENTRA")
    if enviar:
       inserir1(a1,a2,a3,a4)
        
elif escolha=="CONSULTA":
     
     consulta()

elif escolha=="CLASSE":
    computador = Computador("asus", "16GB", "N7vidia")
    st.write(computador.marca)
    

elif escolha=="MAPA":
    from streamlit_folium import st_folium
    mapa = folium.Map(location=[-16.4507341,-54.6498371], zoom_start=17)
    folium.Marker(location=[-16.4507341,-54.6498371], popup='SANEAR', tooltip="Clique aqui", icon=folium.Icon(color="green")).add_to(mapa)
    folium.CircleMarker(location=[-16.4507341,-54.6498371],
                    radius=150,
                    color='red',
                    fill=True,
                    fill_color='red').add_to(mapa)
    st_folium(mapa)
    funcionarios = {
    'Pregao': ['021/2023', '021/2023', '021/2023', '021/2023'],
    'Empresa': ['Conehidro', 'Conehidro', 'Conehidro', 'Conehidro'],
    'NAD': ['994/2023', '1009/2023', '123/2024', '478/2024'],
    }
    mapa = pd.DataFrame(funcionarios)
    st.dataframe(mapa)
   
  




import streamlit as st 
import pandas as pd 


st.set_page_config("Consulta contratos de obra", layout="wide")
colimage = st.columns((1,1,1))
colimage[1].image("logosanear.png", width=300)

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)


def dados():
    n=11
    df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
    st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto", "valor", "fiscal"])])
    #st.write("dados do contrato")

def medicoes():
    df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)
    
    st.write("medicoes")
    

def relatorios():
    st.write('relatorios')



st.sidebar.header("Contratos")
st.sidebar.button("TECNOBOMBAS - 004/2023", use_container_width=True)
st.sidebar.button("MASTER - 028/2023", use_container_width=True)
st.sidebar.button("SPARTACUS", use_container_width=True)

lista_contratos=["TECNOBOMBAS - 004/2023", "MASTER - 028/2023", "SPARTACUS", \
                 "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "MASTER - 034/2022", "SAGATEC", "ELETRIC", \
                 "LEILOEIRA", "DA GARISTO", "TECNBOMBAS - 007/2024", "UPX", "GENTE", "RESUMO"]
lista_dados=["Dados", "Medições", "Relatorios"]

t11, t12, t13 = st.tabs(lista_dados)
with t11:
    dados()

with t12:
    medicoes()

with t13:
    relatorios()
    
    
    
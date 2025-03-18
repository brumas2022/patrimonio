import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt


st.set_page_config("Consulta contratos de obra", layout="wide")
colimage = st.columns((1,1,1))
#colimage[1].image("logosanear.png", width=300)

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)


def dados(n):
    #n=11
    df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
    st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto", "valor", "fiscal"])])
    #st.write("dados do contrato")

def medicoes(n):
    #n=11
    df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    #df_medicao.dtypes
    df_y = df_medicao[df_medicao["CONTRATO"]==nro_contrato].tolist()
    st.dataframe(df_y)
    df_x=[1, 2, 3, 4, 5, 6, 7, 8]
    #df_y=[93264, 89785, 143861, 92502, 192910, 117159, 104735, 101971]
    #st.bar_chart(df_y)
    #print(df_medicao["VALOR"])
    #fig, ax = plt.subplots(figsize = (8,5))
    #ax.bar(df_x, df_y)
    #plt.plot(df_x, df_y)
    #plt.show()
    #df_medicao[df_medicao["CONTRATO"==nro_contrato]]
    #st.dataframe(df_x)
def relatorios():
    st.write('relatorios')

lista_contratos=["TECNOBOMBAS - 004/2023", "MASTER - 028/2023", "SPARTACUS", \
                 "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "MASTER - 034/2022", "SAGATEC", "ELETRIC", \
                 "LEILOEIRA", "DA GARISTO", "TECNBOMBAS - 007/2024", "UPX", "GENTE", "RESUMO"]


st.sidebar.header("Contratos")
a = st.sidebar.button(lista_contratos[0], use_container_width=True)
b = st.sidebar.button(lista_contratos[1], use_container_width=True)
c = st.sidebar.button(lista_contratos[2], use_container_width=True)
d = st.sidebar.button(lista_contratos[3], use_container_width=True)
e = st.sidebar.button(lista_contratos[4], use_container_width=True)
f = st.sidebar.button(lista_contratos[5], use_container_width=True)
g = st.sidebar.button(lista_contratos[6], use_container_width=True)
h = st.sidebar.button(lista_contratos[7], use_container_width=True)
i = st.sidebar.button(lista_contratos[8], use_container_width=True)
j = st.sidebar.button(lista_contratos[9], use_container_width=True)

lista_dados=["Dados", "Medições", "Relatorios"]

if a:
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        dados(11)
    with t12:
        medicoes(11)

    with t13:
        relatorios()

if b:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(10)
   with t12:
       medicoes(10)

   with t13:
       relatorios() 
    
    
    
import streamlit as st 
import pandas as pd 
#import matplotlib.pyplot as plt


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
    df_selecao = df_medicao[df_medicao["CONTRATO"]==nro_contrato]
    st.dataframe(df_selecao, hide_index=True)
    total_medido = df_selecao["VALOR"].sum()
    contrato = df_contratos.iloc[(n,7)]
    saldo = contrato - total_medido
    
    dados = {'total': total_medido, 'saldo': saldo}
    df_dados = pd.DataFrame(dados, index=[0])
    st.dataframe(df_dados.style.format(thousands=".", decimal=","), use_container_width=True, hide_index=True)
    
    #st.write("Total das medições :", total_medido)
    #st.write("Saldo do contrato", saldo)
    
    
    #df_medicao.dtypes
    df_y = df_selecao['VALOR'].tolist()
    #st.dataframe(df_y)
    df_x=[1, 2, 3, 4, 5, 6, 7, 8]
    #df_y=[93264, 89785, 143861, 92502, 192910, 117159, 104735, 101971]
    st.bar_chart(df_y, width=1, use_container_width=True)
    #print(df_medicao["VALOR"])
    #fig, ax = plt.subplots(figsize = (8,5))
    #ax.bar(df_x, df_y)
    #plt.plot(df_x, df_y)
    #plt.show()
    #df_medicao[df_medicao["CONTRATO"==nro_contrato]]
    #st.dataframe(df_x)
def relatorios():
    st.write('Aqui serão colocados os relatorios mensais da obra')
    linha = []
    for number in range(30):
        a = st.text_input(f"Linha {number} :", key=number, label_visibility="collapsed")
        linha.append(a)

lista_contratos=["TECNOBOMBAS - 004/2023", "MASTER - 028/2023", "SPARTACUS", \
                 "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "MASTER - 034/2022", "SAGATEC", "ELETRIC", \
                 "LEILOEIRA", "DA GARISTO", "TECNBOMBAS - 007/2024", "UPX", "GENTE", "MILLENIUM"]


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
k = st.sidebar.button(lista_contratos[10], use_container_width=True)
l = st.sidebar.button(lista_contratos[11], use_container_width=True)
m = st.sidebar.button(lista_contratos[12], use_container_width=True)
n = st.sidebar.button(lista_contratos[13], use_container_width=True)
o = st.sidebar.button(lista_contratos[14], use_container_width=True)
p = st.sidebar.button(lista_contratos[15], use_container_width=True)

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

if c:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(23)
   with t12:
       medicoes(23)

   with t13:
       relatorios()
       
if d:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(24)
   with t12:
       medicoes(24)

   with t13:
       relatorios()
 
if e:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(29)
   with t12:
       medicoes(29)

   with t13:
       relatorios()  
       
if f:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(0)
   with t12:
       medicoes(0)

   with t13:
       relatorios() 
       
if g:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(4)
   with t12:
       medicoes(4)

   with t13:
       relatorios() 

if h:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(13)
   with t12:
       medicoes(13)

   with t13:
       relatorios()
           
if i:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(14)
   with t12:
       medicoes(14)

   with t13:
       relatorios() 

if j:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(19)
   with t12:
       medicoes(19)

   with t13:
       relatorios() 

if k:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(20)
   with t12:
       medicoes(20)

   with t13:
       relatorios()   
       
if l:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(21)
   with t12:
       medicoes(21)

   with t13:
       relatorios()   
       
if m:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(22)
   with t12:
       medicoes(22)

   with t13:
       relatorios()   
       
if n:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(27)
   with t12:
       medicoes(27)

   with t13:
       relatorios() 
       
if o:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(28)
   with t12:
       medicoes(28)

   with t13:
       relatorios() 
       
if p:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(15)
   with t12:
       medicoes(15)

   with t13:
       relatorios() 
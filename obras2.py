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
    df_mostra_dados = df_contratos.loc[(n, ["contrato", "empresa", "objeto", "valor", "fiscal", "inicio", "fim"])]
    st.dataframe(df_mostra_dados)
    
    #st.write("dados do contrato")

def medicoes(n):
    #n=11
    df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_selecao = df_medicao[df_medicao["CONTRATO"]==nro_contrato]
    df_selecao["%ACULUMADO"]=df_selecao["VALOR"].cumsum()
    df_selecao["%PERCENTUUAL DO CONTRATO"]=(df_selecao["VALOR"].cumsum()/df_contratos["valor"])*100
    st.dataframe(df_selecao, hide_index=True)
    total_medido = df_selecao["VALOR"].sum()
    contrato = df_contratos.iloc[(n,7)]
    saldo = contrato - total_medido
    
    porcento = "indisponivel" #(total_medido / df_contratos['valor'])*100
    
    dados = {'TOTAL MEDIDO': total_medido, 'PERCENTUAL EXECUTADO': porcento, 'SALDO DO CONTRATO': saldo}
    df_dados = pd.DataFrame(dados, index=[0])
    st.dataframe(df_dados.style.format(thousands=".", decimal=","), width=500, use_container_width=False, hide_index=True)
    
    #st.write("Total das medições :", total_medido)
    #st.write("Saldo do contrato", saldo)
    
    
    #df_medicao.dtypes
    df_y = df_selecao['VALOR'].tolist()
    #st.dataframe(df_y)
    df_x=[1, 2, 3, 4, 5, 6, 7, 8]
    #df_y=[93264, 89785, 143861, 92502, 192910, 117159, 104735, 101971]
    st.bar_chart(df_y, width=750, use_container_width=False)
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

lista_contratos=["TECNOBOMBAS - 004/2023(11)", "MASTER - 028/2023(10)", "SPARTACUS(23)", \
                 "MENEGUETI(24)", "GEOPOÇOS(29)", "ALPHA(0)", "SM7(4)", "MASTER - 034/2022(13)", "SAGATEC(14)", "ELETRIC(19)", \
                 "LEILOEIRA(20)", "DA GARISTO(21)", "TECNBOMBAS - 007/2024(22)", "UPX(27)", "GENTE(28)", "MILLENIUM - 008/2023(15)", "MILLENIUM - 009/2023(16)", \
                 "MILLENIUM - 003/2024(17)", "MASTER 019-2024(33)", "DIMBEL(35)", "COOMSER OBRA(34)", "MILLENIUM 017-2024(37)", "MARCIO SOUZA FARIAS(38)"]

lista_contratos_OBRAS = ["MASTER - 034/2022(13)", "MASTER - 028/2023(10)", "MASTER 019-2024(33)", "MENEGUETI(24)", "TECNBOMBAS - 007/2024(22)", \
                         "SPARTACUS(39)", "MILLENIUM - 009/2023(16)", "MILLENIUM - 003/2024(17)", "MILLENIUM 017-2024(37)", "MILLENIUM - 008/2023(15)", \
                         "COOMSER OBRA(34)", "SPARTACUS(23)", "SM7(4)", "RST ENGENHARIA(3)", "MARCIO SOUZA FARIAS(38)",  "DIMBEL(35)", "DA GARISTO(21)"]
st.sidebar.header("Contratos")
a = st.sidebar.button(lista_contratos_OBRAS[0], use_container_width=True)
b = st.sidebar.button(lista_contratos_OBRAS[1], use_container_width=True)
c = st.sidebar.button(lista_contratos_OBRAS[2], use_container_width=True)
d = st.sidebar.button(lista_contratos_OBRAS[3], use_container_width=True)
e = st.sidebar.button(lista_contratos_OBRAS[4], use_container_width=True)
f = st.sidebar.button(lista_contratos_OBRAS[5], use_container_width=True)
g = st.sidebar.button(lista_contratos_OBRAS[6], use_container_width=True)
h = st.sidebar.button(lista_contratos_OBRAS[7], use_container_width=True)
i = st.sidebar.button(lista_contratos_OBRAS[8], use_container_width=True)
j = st.sidebar.button(lista_contratos_OBRAS[9], use_container_width=True)
k = st.sidebar.button(lista_contratos_OBRAS[10], use_container_width=True)
l = st.sidebar.button(lista_contratos_OBRAS[11], use_container_width=True)
m = st.sidebar.button(lista_contratos_OBRAS[12], use_container_width=True)
n = st.sidebar.button(lista_contratos_OBRAS[13], use_container_width=True)
o = st.sidebar.button(lista_contratos_OBRAS[14], use_container_width=True)
p = st.sidebar.button(lista_contratos_OBRAS[15], use_container_width=True)
q = st.sidebar.button(lista_contratos_OBRAS[16], use_container_width=True)
r = st.sidebar.button(lista_contratos_OBRAS[17], use_container_width=True)
s = st.sidebar.button(lista_contratos_OBRAS[18], use_container_width=True)

lista_dados=["Dados", "Medições", "Relatorios"]

if a:
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        dados(13)
    with t12:
        medicoes(13)
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
       dados(33)
   with t12:
       medicoes(33)

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
       dados(22)
   with t12:
       medicoes(22)

   with t13:
       relatorios()  
       
if f:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(39)
   with t12:
       medicoes(39)

   with t13:
       relatorios() 
       
if g:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(16)
   with t12:
       medicoes(16)

   with t13:
       relatorios() 

if h:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(17)
   with t12:
       medicoes(17)

   with t13:
       relatorios()
           
if i:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(37)
   with t12:
       medicoes(37)

   with t13:
       relatorios() 

if j:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(15)
   with t12:
       medicoes(15)

   with t13:
       relatorios() 

if k:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(34)
   with t12:
       medicoes(34)

   with t13:
       relatorios()   
       
if l:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(23)
   with t12:
       medicoes(23)

   with t13:
       relatorios()   
       
if m:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(4)
   with t12:
       medicoes(4)

   with t13:
       relatorios()   
       
if n:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(3)
   with t12:
       medicoes(3)

   with t13:
       relatorios() 
       
if o:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(38)
   with t12:
       medicoes(38)

   with t13:
       relatorios() 
       
if p:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(35)
   with t12:
       medicoes(35)

   with t13:
       relatorios() 
       
if q:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(21)
   with t12:
       medicoes(21)

   with t13:
       relatorios() 
       
if r:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(17)
   with t12:
       medicoes(17)

   with t13:
       relatorios() 
       
if s:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(33)
   with t12:
       medicoes(33)

   with t13:
       relatorios() 
       
if t:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(35)
   with t12:
       #medicoes(35)
       pass

   with t13:
       relatorios() 
       
if u:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(34)
   with t12:
       medicoes(34)
       #pass

   with t13:
       relatorios()
       
if v:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(37)
   with t12:
       medicoes(37)
       #pass

   with t13:
       relatorios()
       
if x:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(38)
   with t12:
       #medicoes(38)
       pass

   with t13:
       relatorios()
import streamlit as st 
import pandas as pd 
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import openpyxl
#import matplotlib.pyplot as plt


st.set_page_config("Consulta contratos de obra", layout="wide")
colimage = st.columns((1,1,1))
#colimage[1].image("logosanear.png", width=300)

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=4)
df_medicao1  = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=0)

def bd_entrada():
    load_dotenv()
    url = os.getenv("supabase_url")
    key = os.getenv("supabase_key")

    supabase: Client = create_client(url, key)

    resposta = supabase.table("bdmedicaonova").select("contrato").execute()
    st.dataframe(resposta.data)

    # fazer a conexao do banco de dados supa com o dotenv
    pass

def ctr_excel():
        #df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
        df_contratos = pd.read_excel("relatorio_contratos.xlsx")
        #choice_ctr = df_contratos["contrato"]
        choice_ctr = df_contratos["Contrato"]
        return choice_ctr

def empresa():
        #df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
        df_contratos = pd.read_excel("relatorio_contratos.xlsx")
        #empresa = df_contratos["empresa"]
        empresa = df_contratos["Fornecedor"]
        return empresa

def main():
        df = pd.concat([ctr_excel(), empresa()], axis=1)
        #st.dataframe(df)
        choice = st.sidebar.radio("OPCOES", options=df.itertuples(), format_func=lambda x : f"{x.Contrato} - {str(x.Fornecedor)[:20]}")
        lista_de_dados = ["Dados", "Medicoes", "Aditivos", "Graficos"]
        t1,t2,t3, t4 = st.tabs(lista_de_dados)
        with t1:
            #as duas linhas abaixo usa o supabase e mostra todos os dados de cada contrato
            #response1 = supabase.table("bdmedicaonova").select("contrato").eq("contrato", choice).execute()
            #st.dataframe(response1.data)


            #Aqui usamos a tabela em excel para mostrar os dados do contrato
            #df_dados = pd.read_excel("DADOS_CONTRATOS.xlsx")
            df_dados = pd.read_excel("relatorio_contratos.xlsx")
            df_mostra_dados = df_dados[df_dados['Contrato']==choice.Contrato]
        
            st.markdown(f"**CONTRATO** : {df_mostra_dados.values[0,0]}")
            st.markdown(f"**EMPRESA** :  {df_mostra_dados.values[0,3]}")
            st.markdown(f"**OBJETO** : {df_mostra_dados.values[0,2]}")
            st.markdown(f"**VALOR** : {df_mostra_dados.values[0,4]}")
            #st.markdown(f"**FISCAL** : {df_mostra_dados.values[0,10]}", )
            #st.markdown(f"**INICIO** : {df_mostra_dados.values[0,5].strftime("%d/%m/%Y")}")
            #st.markdown(f"**FIM** : {df_mostra_dados.values[0,6].strftime("%d/%m/%Y")}")
            st.markdown(f"**SITUAÇÃO** : {df_mostra_dados.values[0,9]}")


        with t2:
           ctr = choice.Contrato[5:]
           st.write(ctr)
           response1 = supabase.table("bdmedicaonova").select("contrato", "medicao", "datamedicao").eq("contrato", ctr).execute()
           st.dataframe(response1.data)
        with t3:
            st.write("ADITIVOS")
    
        with t4:
            st.write("GRAFICOS")






#def entrada_supa():


#    #url: str = os.environ.get("https://hdhvkseneldllvnlvpgc.supabase.co")
#    #key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkaHZrc2VuZWxkbGx2bmx2cGdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTM3MDM4NTEsImV4cCI6MjAwOTI3OTg1MX0.2Mv5sip2DTHrYY-Ar4WbPNISb1Z3Gtbc9ErhnlohPOM")


#    supabase: Client = create_client("https://hdhvkseneldllvnlvpgc.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkaHZrc2VuZWxkbGx2bmx2cGdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTM3MDM4NTEsImV4cCI6MjAwOTI3OTg1MX0.2Mv5sip2DTHrYY-Ar4WbPNISb1Z3Gtbc9ErhnlohPOM")

#    def lista_contratos():
#        resposta = supabase.table("bdmedicaonova").select("contrato").execute()

#        olhar = resposta.model_dump()

#        lista = [ ]
#        i=0
#        for i in range(100):
#            a = olhar['data'][i]['contrato']
#            lista.append(a)
#        return list(set(lista))










   

#    main()
   
   
   
   


def dados(n):
    #n=11
    
    
    df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
    df_mostra_dados = df_contratos.loc[(n, ["contrato", "empresa", "objeto", "valor", "fiscal", "inicio", "fim"])]
    valor_contrato = "R$ {:_.2f}".format(df_mostra_dados.values[3])
    valor_contrato_brasileiro = valor_contrato.replace(".",",").replace("_",".")
    
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_aditivo = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=1)
    df_aditivo1 = df_aditivo[df_aditivo["CONTRATO"]==nro_contrato]
    
    st.markdown(f"**CONTRATO** : {df_mostra_dados.values[0]}")
    st.markdown(f"**EMPRESA** :  {df_mostra_dados.values[1]}")
    st.markdown(f"**OBJETO** : {df_mostra_dados.values[2]}")
    st.markdown(f"**VALOR** : {valor_contrato_brasileiro}")
    st.markdown(f"**FISCAL** : {df_mostra_dados.values[4]}", )
    st.markdown(f"**INICIO** : {df_mostra_dados.values[5].strftime("%d/%m/%Y")}")
    st.markdown(f"**FIM** : {df_mostra_dados.values[6].strftime("%d/%m/%Y")}")
    st.write("---")
    st.markdown("**ADITIVOS**")
    st.dataframe(df_aditivo1)
    
    
    

def medicoes(n):
    #n=11
    #df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=4)
    df_medicao  = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=0)
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_selecao = df_medicao[df_medicao["CONTRATO"]==nro_contrato]
    
    valor_contrato = df_contratos.loc[(n, ["valor"])]
    
    df_selecao["%ACULUMADO"]=df_selecao["VALOR"].cumsum()
    
    df_selecao["%PERCENTUUAL DO CONTRATO"]=(df_selecao["VALOR"].cumsum()/float(valor_contrato))*100
    
    #st.dataframe(df_selecao, hide_index=True)
    st.dataframe(df_selecao, hide_index=True, column_config={
        "DATA MEDICAO": st.column_config.DatetimeColumn(
            "DATA MEDICAO",
            format="DD/MM/YYYY",
            
        ),
        "DATA NF": st.column_config.DatetimeColumn(
            "DATA NF",
            format="DD/MM/YYYY",
            
        ),
        "DATA PAGTO": st.column_config.DatetimeColumn(
            "DATA PAGTO",
            format="DD/MM/YYYY",
            
        ),
        #"NF": st.column_config.NumberColumn(
        #    "NF",
        #    help="NOTA FISCAL EMITIDA",
        #    format="plain",
            
        #),
    })
    
    
    total_medido = df_selecao["VALOR"].sum()
    contrato = df_contratos.iloc[(n,7)]
    saldo = contrato - total_medido
    
    porcento = (total_medido / float(valor_contrato))*100
    
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
    df = pd.read_excel("relatorio.xlsx", sheet_name=0)
    st.dataframe(df)
    
    
    
lista_contratos=["TECNOBOMBAS - 004/2023", "MASTER - 028/2023", "SPARTACUS", \
                 "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "MASTER - 034/2022", "SAGATEC", "ELETRIC", \
                 "LEILOEIRA", "DA GARISTO", "TECNBOMBAS - 007/2024", "UPX", "GENTE", "MILLENIUM - 008/2023", "MILLENIUM - 009/2023", \
                 "MILLENIUM - 003/2024", "MASTER 019-2024", "DIMBEL", "COOMSER OBRA", "MILLENIUM 017-2024", "MARCIO SOUZA FARIAS", "DIEFRA"]


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
q = st.sidebar.button(lista_contratos[16], use_container_width=True)
r = st.sidebar.button(lista_contratos[17], use_container_width=True)
s = st.sidebar.button(lista_contratos[18], use_container_width=True)
t = st.sidebar.button(lista_contratos[19], use_container_width=True)
u = st.sidebar.button(lista_contratos[20], use_container_width=True)
v = st.sidebar.button(lista_contratos[21], use_container_width=True)
x = st.sidebar.button(lista_contratos[22], use_container_width=True)
w = st.sidebar.button(lista_contratos[23], use_container_width=True)

lista_dados=["Dados", "Medições", "Relatorios"]

if a:
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        dados(11)
    with t12:
        medicoes(11)

    with t13:
        main()

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
       
if q:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(16)
   with t12:
       medicoes(16)

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

if w:
   t11, t12, t13 = st.tabs(lista_dados)
   with t11:
       dados(40)
   with t12:
       #medicoes(38)
       pass

   with t13:
       relatorios()

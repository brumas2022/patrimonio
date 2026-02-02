import streamlit as st 
import pandas as pd 
import datetime
#import matplotlib.pyplot as plt


st.set_page_config("Consulta contratos de obra", layout="wide")
colimage = st.columns((1,1,1))
#colimage[1].image("logosanear.png", width=300)

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
#df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=4)
df_medicao  = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=0)



def vencimentos():
    contratos_vencer = pd.read_excel("janeiro-2026.xlsx", sheet_name=0)
    st.markdown("**CONTRATOS A VENCER EM JANEIRO/2026**")
    st.dataframe(contratos_vencer)
    

def aditivos(n):
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_aditivo = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=1)
    df_aditivo1 = df_aditivo[df_aditivo["CONTRATO"]==nro_contrato]

    
    st.markdown("**ADITIVOS**")
    #st.dataframe(df_aditivo1)
    st.dataframe(df_aditivo1, hide_index=False, column_config={
        "DATA": st.column_config.DatetimeColumn(
            "DATA",
            format="DD/MM/YYYY",
            
        ),
        "EXECUCAO INICIA": st.column_config.DatetimeColumn(
            "EXECUCAO INICIA",
            format="DD/MM/YYYY",
            
        ),
        "EXECUCAO FINAL": st.column_config.DatetimeColumn(
            "EXECUCAO FINAL",
            format="DD/MM/YYYY",
            
        ),
        "VIGENCIA INICIAL": st.column_config.DatetimeColumn(
            "VIGENCIA INICIAL",
            format="DD/MM/YYYY",
            
        ),
        "VIGENCIA FINAL": st.column_config.DatetimeColumn(
            "VIGENCIA FINAL",
            format="DD/MM/YYYY",
            
        ),
        #"NF": st.column_config.NumberColumn(
        #    "NF",
        #    help="NOTA FISCAL EMITIDA",
        #    format="plain",
            
        #),
    })


def dados(n):
    
    df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
    df_mostra_dados = df_contratos.loc[(n, ["contrato", "empresa", "objeto", "valor", "fiscal", "inicio", "fim", "situacao"])]
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
    #st.markdown(f"**SITUAÇÃO** : {df_mostra_dados.values[14]}")
    
    #hoje = datetime.date.today().strftime("%d/%m/%Y") 
    #data_fim = df_mostra_dados.values[6].strftime("%d/%m/%Y")
    #if hoje > data_fim:
    #    st.markdown(f"Este contrato venceu. Informe o fiscal de contrato")

    
    

def medicoes(n):
    #n=11
    #df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=4)
    df_medicao  = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=0)
    #df_medicao
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_selecao = df_medicao[df_medicao["CONTRATO"]==nro_contrato]
    #df_selecao = df_medicao[df_medicao["contrato"]==nro_contrato]

        
    valor_contrato = df_contratos.loc[(n, ["valor"])]
    
    df_selecao["%ACUMULADO"]=df_selecao['VALOR'].cumsum()
    
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
    df_aditivo = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=1)
    #total_b = df[df['Produto'] == 'B']['Vendas'].sum()
    valor_aditivos = df_aditivo[df_aditivo["TIPO"]=="ADITIVO DE VALOR"]['VALOR'].sum()
    contrato = df_contratos.iloc[(n,7)] + valor_aditivos
    
    saldo = contrato - total_medido
   
    
    porcento = (total_medido / float(valor_contrato))*100
    print(total_medido)
    print(df_contratos.loc[(n, ["valor"])])
    
    dados = {'TOTAL MEDIDO': total_medido, 'PERCENTUAL EXECUTADO': porcento, 'SALDO DO CONTRATO': saldo}
    df_dados = pd.DataFrame(dados, index=[0])
    st.dataframe(df_dados.style.format(thousands=".", decimal=","), width=500, use_container_width=False, hide_index=True)
    
    
    #st.write("Total das medições :", total_medido)
    #st.write("Saldo do contrato", saldo)
    
    
    #df_medicao.dtypes
    #df_y = df_selecao['VALOR'].tolist()
    #st.dataframe(df_y)
    #df_x=[1, 2, 3, 4, 5, 6, 7, 8]
    #df_y=[93264, 89785, 143861, 92502, 192910, 117159, 104735, 101971]
    #st.bar_chart(df_y, width=750, use_container_width=False)
    #print(df_medicao["VALOR"])
    #fig, ax = plt.subplots(figsize = (8,5))
    #ax.bar(df_x, df_y)
    #plt.plot(df_x, df_y)
    #plt.show()
    #df_medicao[df_medicao["CONTRATO"==nro_contrato]]
    #st.dataframe(df_x)

def graficos(n):
    df_medicao  = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=0)
    nro_contrato = f"{df_contratos.iloc[n,1]}"
    df_selecao = df_medicao[df_medicao["CONTRATO"]==nro_contrato]
    df_y = df_selecao['VALOR'].tolist()
    #st.dataframe(df_y)
    df_x=[1, 2, 3, 4, 5, 6, 7, 8]
    #df_y=[93264, 89785, 143861, 92502, 192910, 117159, 104735, 101971]
    st.bar_chart(df_y, width=750, use_container_width=False)

def supa_medicoes():
    import os
    from supabase import create_client, Client
    from dotenv import load_dotenv
    load_dotenv()

    url = os.getenv("URL")
    key = os.getenv("KEY")

    supabase: Client = create_client(url, key)

    consulta = supabase.table("bdmedicaonova").select("*").eq("contrato", "009/2022").execute()

    st.dataframe(consulta.data)


def relatorios():

    st.write('Aqui serão colocados os relatorios mensais da obra')
    linha = []
    for number in range(30):
        a = st.text_input(f"Linha {number} :", key=number, label_visibility="collapsed")
        linha.append(a)
    #supa_medicoes()

lista_contratos=["TECNOBOMBAS - 004/2023(11)", "MASTER - 028/2023(10)", "SPARTACUS(23)", \
                 "MENEGUETI(24)", "GEOPOÇOS(29)", "ALPHA(0)", "SM7(4)", "MASTER - 034/2022(13)", "SAGATEC(14)", "ELETRIC(19)", \
                 "LEILOEIRA(20)", "DA GARISTO(21)", "TECNBOMBAS - 007/2024(22)", "UPX(27)", "GENTE(28)", "MILLENIUM - 008/2023(15)", "MILLENIUM - 009/2023(16)", \
                 "MILLENIUM - 003/2024(17)", "MASTER 019-2024(33)", "DIMBEL(35)", "COOMSER OBRA(34)", "MILLENIUM 017-2024(37)", "MARCIO SOUZA FARIAS(38)"]

lista_contratos_OBRAS = ["MASTER - 034/2022", "MASTER - 028/2023", "ALPHA", "CONSTRUTORA MENEGUETI - VG", "TECNBOMBAS - 007/2024", "TECNOBOMBAS - 004/2023", \
                         "SPARTACUS - 024/2024", "MILLENIUM - 009/2023", "MILLENIUM - 003/2024", "MILLENIUM - 017/2024", "MILLENIUM - 008/2023", \
                         "COOMSER OBRA", "SPARTACUS - 013/2024", "SM7 - TANKS BR", "RST ENGENHARIA", "MARCIO SOUZA FARIAS",  "DIMBEL", "DA GARISTO", "ENRON", "RONDOFONE", "SOLOS", "R.SANTANA"]
st.sidebar.header("Contratos de obras")
a = st.sidebar.button(lista_contratos_OBRAS[0], use_container_width=True) 
b = st.sidebar.button(lista_contratos_OBRAS[1], use_container_width=True)
c = st.sidebar.button(lista_contratos_OBRAS[2], use_container_width=True)
d = st.sidebar.button(lista_contratos_OBRAS[3], use_container_width=True)
e = st.sidebar.button(lista_contratos_OBRAS[4], use_container_width=True)
f1 = st.sidebar.button(lista_contratos_OBRAS[5], use_container_width=True)
f = st.sidebar.button(lista_contratos_OBRAS[6], use_container_width=True)
g = st.sidebar.button(lista_contratos_OBRAS[7], use_container_width=True)
h = st.sidebar.button(lista_contratos_OBRAS[8], use_container_width=True)
i = st.sidebar.button(lista_contratos_OBRAS[9], use_container_width=True)
j = st.sidebar.button(lista_contratos_OBRAS[10], use_container_width=True)
k = st.sidebar.button(lista_contratos_OBRAS[11], use_container_width=True)
l = st.sidebar.button(lista_contratos_OBRAS[12], use_container_width=True)
m = st.sidebar.button(lista_contratos_OBRAS[13], use_container_width=True)
#n = st.sidebar.button(lista_contratos_OBRAS[14], use_container_width=True)
#o = st.sidebar.button(lista_contratos_OBRAS[15], use_container_width=True)
#p = st.sidebar.button(lista_contratos_OBRAS[16], use_container_width=True)
#q = st.sidebar.button(lista_contratos_OBRAS[17], use_container_width=True)
r = st.sidebar.button(lista_contratos_OBRAS[18], use_container_width=True)
s = st.sidebar.button(lista_contratos_OBRAS[19], use_container_width=True)
t = st.sidebar.button(lista_contratos_OBRAS[20], use_container_width=True)
u = st.sidebar.button(lista_contratos_OBRAS[21], use_container_width=True)

lista_dados=["Dados", "Medições", "Aditivos", "Gráfico"]

if a:
    t11, t12, t13, t14 = st.tabs(lista_dados)
    with t11:
        dados(13)
    with t12:
        medicoes(13)
    with t13:
        aditivos(13)
    with t14:
        graficos(13)
elif b:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(10)
   with t12:
       medicoes(10)

   with t13:
       aditivos(10) 
   with t14:
       graficos(10) 

elif c:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(0)
   with t12:
       medicoes(0)

   with t13:
       aditivos(0)
   with t14:
       graficos(0)
       
elif d:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(24)
   with t12:
       medicoes(24)

   with t13:
       aditivos(24)
   with t14:
       graficos(24) 
 
elif e:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(22)
   with t12:
       medicoes(22)

   with t13:
       aditivos(22)
   with t14:
       graficos(22)    
       
elif f:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(39)
   with t12:
       medicoes(39)

   with t13:
       aditivos(30) 
   with t14:
       graficos(30) 

elif f1:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(11)
   with t12:
       medicoes(11)

   with t13:
       aditivos(11)
   with t14:
       graficos(11)  
       
elif g:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(16)
   with t12:
       medicoes(16)

   with t13:
       aditivos(16) 
   with t14:
       graficos(16) 

elif h:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(17)
   with t12:
       medicoes(17)

   with t13:
       aditivos(17)
   with t14:
       graficos(17) 
           
elif i:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(37)
   with t12:
       medicoes(37)

   with t13:
       aditivos(37)
   with t14:
       graficos(37) 

elif j:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(15)
   with t12:
       medicoes(15)

   with t13:
       aditivos(15)
   with t14:
       graficos(15)  

elif k:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(34)
   with t12:
       medicoes(34)

   with t13:
       aditivos(34) 
   with t14:
       graficos(34)   
       
elif l:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(23)
   with t12:
       medicoes(23)

   with t13:
       aditivos(23)
   with t14:
       graficos(23)    
       
elif m:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(4)
   with t12:
       medicoes(4)

   with t13:
       aditivos(4)
   with t14:
       graficos(4)   
       
#elif n:
#   t11, t12, t13, t14 = st.tabs(lista_dados)
#   with t11:
#       dados(3)
#   with t12:
#       medicoes(3)

#   with t13:
#       aditivos(3)
#   with t14:
#       graficos(3)  
       
# elif o:
#    t11, t12, t13, t14 = st.tabs(lista_dados)
#    with t11:
#        dados(38)
#    with t12:
#        medicoes(38)

#    with t13:
#        aditivos(38)
#    with t14:
#        graficos(38) 
       
# elif p:
#    t11, t12, t13, t14 = st.tabs(lista_dados)
#    with t11:
#        dados(35)
#    with t12:
#        medicoes(35)

#    with t13:
#        aditivos(35) 
#    with t14:
#        graficos(35) 
       
# elif q:
#    t11, t12, t13, t14 = st.tabs(lista_dados)
#    with t11:
#        dados(21)
#    with t12:
#        medicoes(21)

#    with t13:
#        aditivos(21)
#    with t14:
#        graficos(21)  

elif r:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(45)
   with t12:
       medicoes(45)

   with t13:
       aditivos(45) 
   with t14:
       graficos(45) 

elif s:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(46)
   with t12:
       medicoes(46)

   with t13:
       aditivos(46)
   with t14:
       graficos(46)  

elif t:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(47)
   with t12:
       medicoes(47)

   with t13:
       aditivos(47) 
   with t14:
       graficos(47) 

elif u:
   t11, t12, t13, t14 = st.tabs(lista_dados)
   with t11:
       dados(48)
   with t12:
       medicoes(48)

   with t13:
       aditivos(48)
   with t14:
       graficos(48) 

else:
    #st.image("contratos/Logosanear1.jpg")
    vencimentos()


#vencimentos()
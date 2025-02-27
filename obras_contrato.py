import streamlit as st 
import pandas as pd

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=2)

st.set_page_config("Consulta contratos de obra", layout="wide")
lista_contratos=["TECNOBOMBAS", "MASTER", "SPARTACUS", "MENEGUETI", "MILLENIUM"]
lista_dados=["Dados", "Medições", "Relatorios"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(lista_contratos)
with tab1:
    
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        st.write("Contrado Nro")
        n=11
        col = st.columns((1,1,1))
        nro_contrato = col[0].text_input("CONTRATO/ANO", value=f"{df_contratos.iloc[n,1]}")
        empresa = col[0].text_input("EMPRESA", value=f"{df_contratos.iloc[n,2]}")
        objeto = col[0].text_input("OBJETO", value=f"{df_contratos.iloc[n,3]}")
        valor = col[0].text_input("VALOR", value=f"{df_contratos.iloc[n,7]}")
        data_inicio = col[0].text_input("DATA INICIAL", value=f"{df_contratos.iloc[n,4].strftime("%d/%m/%Y")}")
        data_fim = col[0].text_input("DATA FINAL", value=f"{df_contratos.iloc[n,5].strftime("%d/%m/%Y")}")
        
        ordem_inicio = col[1].text_input("Data da ordem de inicio", value= f"{df_contratos.iloc[n,14]}")
        
        
    with t12:
        st.write("Medição nro")
        st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
        
    with t13:
        st.write("Relatorio")
        
with tab2:
    t21, t22, t23 = st.tabs(lista_dados) 
    t21.subheader("Contrato 007/2024", divider="blue")
    
    with t21:
        st.write("Contrado Nro")
    with t22:
        st.write("Medição nro")
    with t23:
        st.write("Relatorio")
        
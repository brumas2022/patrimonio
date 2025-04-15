import streamlit as st
import pandas as pd
import streamlit_pdf_viewer

st.set_page_config("Obra da Estação de Tratamento de Água 2", layout="wide")

a = st.sidebar.button("PROJETOS")
b = st.sidebar.button("LICITACAO")
c = st.sidebar.button("OBRA")
d = st.sidebar.button("PENDENCIAS DA OBRA")
e = st.sidebar.button("PENDENCIAS DA ETA 2")

if a:
    c = st.selectbox("QUAL PROJETO", ("FLOCULADOR", "DECANTADOR"))
    
    if c=="FLOCULADOR":
       st.write("Este é o projeto do floculador") 
       st.image("floculador-decantador.jpg")
    
    if c=="DECANTADOR":
        st.write("ESTE É O PRJETO DECANTADOR")
        
if b:
    
    st.info("AMPLIAÇÃO DO SISTEMA DE ABASTECIMETNO DE ÁGUA NA ESTAÇÃO DE TRATAMENTO DE ÁGUA (ETA)")
   
    df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=2)
    df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2"]
    st.dataframe(df_medicao.iloc[3:8], hide_index=True)
    st.markdown(":green[Em 19/03/2025 - Chegou Registro de gaveta DN 600]")
    with open("PREGAO 13.xlsx", "rb") as file: 
       st.download_button(label='PLANILHA ORIGINAL', data=file, file_name="PREGAO 13.xlsx") 
        
        
                     

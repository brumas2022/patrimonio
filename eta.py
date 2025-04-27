import streamlit as st
import pandas as pd
import streamlit_pdf_viewer as stf

st.set_page_config("Obra da Estação de Tratamento de Água 2", layout="wide")

def projetos():
    st.info("PROJETOS DA ETA")
    op_proj = ["FLOCULADOR", "DECANTADOR"]
    tab1, tab2 = st.tabs(op_proj)
    
    with tab1:
       st.image("floculador-decantador.JPG")
       #arquivo = stf.pdf_viewer("PLANILHA PREGÃO LOTEAMENTOS.pdf", )
       #st.write(arquivo)
       
    
    with tab2:
        arquivo2 = stf.pdf_viewer("PLANILHA PREGÃO LOTEAMENTOS.pdf")
        return(st.write(arquivo2))
        

a = st.sidebar.button("PROJETOS")
b = st.sidebar.button("LICITACAO")
c = st.sidebar.button("OBRA")
d = st.sidebar.button("PENDENCIAS DA OBRA")
e = st.sidebar.button("PENDENCIAS DA ETA 2")

if a:
    projetos()
        
elif b:
    
    st.info("AMPLIAÇÃO DO SISTEMA DE ABASTECIMETNO DE ÁGUA NA ESTAÇÃO DE TRATAMENTO DE ÁGUA (ETA)")
   
    df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=2)
    df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2"]
    st.dataframe(df_medicao.iloc[3:8], hide_index=True)
    st.markdown(":green[Em 19/03/2025 - Chegou Registro de gaveta DN 600]")
    st.markdown(":red[Em 24/04/2025 - Chegou Registro de gaveta DN 800]")
    ata = st.button("Ata de Registro")
    if ata:
         arquivo1 = stf.pdf_viewer("Ata_de_Registro_de_Precos_-_Pregao_Eletronico_012.2024__assinado.pdf")
         st.markdown(arquivo1)

elif d:
    df_func_1 = pd.read_excel("interligacoes-ETA.xlsx", sheet_name=0)
    df_func_2 = pd.read_excel("interligacoes-ETA.xlsx", sheet_name=1)
    opcoes = ["INTERLIGACAO SAIDA ETA", "INTERLIGACAO CALHA PARSHAL"]
    t1, t2 = st.tabs(opcoes)
    with t1:
        st.dataframe(df_func_1, hide_index=True)
        
    with t2:
        st.dataframe(df_func_2, hide_index=True)
        
        
elif e:
    st.info("ACOES PARA OPERACIONALIZACAO DA ETA II")
    df_operacao = pd.read_excel("interligacoes-ETA.xlsx", sheet_name=3)
    st.dataframe(df_operacao, hide_index=True)
        
    
    
    
        
        
                     

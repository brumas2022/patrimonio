import streamlit as st
import pandas as pd
import streamlit_pdf_viewer as stf

st.set_page_config("Obra da Estação de Tratamento de Água 2", layout="wide")

def projetos():
    st.info("PROJETOS DA ETA")
    projeto = st.selectbox("QUAL PROJETO", ("FLOCULADOR", "DECANTADOR"))
    
    if projeto=="FLOCULADOR":
       st.write("Este é o projeto do floculador") 
       arquivo = stf.pdf_viewer("PLANILHA PREGÃO LOTEAMENTOS.pdf", )
       return(st.write(arquivo))
       
    
    if projeto=="DECANTADOR":
        st.write("ESTE É O PRJETO DECANTADOR")
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
    opcoes = ["INTERLIGACAO SAIDA ETA", "INTERLIGACAO CALHA PARSHAL"]
    selecao = st.selectbox("Escolha", opcoes, index=1)
    if selecao==opcoes[0]:
        #arquivo = stf.pdf_viewer("PROJETO SAIDA ETA.pdf")
        #st.markdown(arquivo)
        df_func = pd.read_excel("interligacoes-ETA.xlsx", sheet_name=0)
        st.dataframe(df_func, hide_index=True)
        joao = st.button("Pare")
    else :
        st.markdown("Calha")
        luis = st.button("PAre")
        
elif e:
    st.info("ACOES PARA OPERACIONALIZACAO DA ETA II")
    df_operacao = pd.read_excel("interligacoes-ETA.xlsx", sheet_name=3)
    st.dataframe(df_operacao, hide_index=True)
        
    
    
    
        
        
                     

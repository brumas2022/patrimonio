import streamlit as st 
import pandas as pd 

def acesso():
    form = st.form(key="Caes", clear_on_submit=True)
    with form:
        lista = ["marcos", "maria", "pitoca"]
        email = st.text_input("Qual o seu nome")
        a=st.text_input("Entre com a senha", type="password" )
        b="102030"
        botao_submit = form.form_submit_button("Confirma!")
        if a==b and email in lista:
            st.write(f"{email}, acesso liberado!!!")
            #st.dataframe(df.iloc[3:], hide_index=True)
            #st.image("img.png")
        if a!="":
            st.write(f"{email}, a senha está incorreta. Verifique como desenvolvedor do produto")

def nova_medicao():
    df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
    df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)
    
    df_nro_contrato = df_contratos['contrato'].to_list()
  
    
    nro = st.sidebar.selectbox("Escolha o contrato", df_nro_contrato)
    resultado = df_medicao.loc[df_medicao['CONTRATO']==nro]
    st.dataframe(resultado, hide_index=True)
    
    
            
acesso()
nova_medicao()
    
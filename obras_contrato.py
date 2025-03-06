import streamlit as st 
import pandas as pd
import os

def senha():
    form = st.form(key="Obras", clear_on_submit=True)
    with form:
        lista = ["marcos", "maria", "pitoca"]
        email = st.text_input("Qual o seu nome")
        a=st.text_input("Entre com a senha", type="password" )
        b="102030"
        botao_submit = form.form_submit_button("Confirma!")
        if a==b and email in lista:
            st.write(f"{email}, acesso liberado!!!")
            #st.dataframe(df.iloc[3:], hide_index=True)
        if a!="":
             st.write(f"{email}, a senha está incorreta. Verifique como desenvolvedor do produto")

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)

st.set_page_config("Consulta contratos de obra", layout="wide")

#senha()

lista_contratos=[":clipboard: TECNOBOMBAS", " :blue [MASTER]", "SPARTACUS", "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "RESUMO"]
lista_dados=["Dados", "Medições", "Relatorios"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(lista_contratos)
with tab1:
    
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        
        n=11
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        
        #open = st.button("Abrir arquivo")
        #if open:
        #    os.startfile('PLANILHA PREGÃO LOTEAMENTOS.pdf')
    with t12:
        st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
        #df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        #st.dataframe(df_selecao)
    with t13:
       st.dataframe(df_contratos.loc[(11, ["contrato", "empresa", "objeto"])])
       
        
with tab2:
    t21, t22, t23 = st.tabs(lista_dados) 
       
    with t21:
        n=10
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        
    with t22:
        st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t23:
        st.write("Relatorio")
        
with tab3:
    t31, t32, t33 = st.tabs(lista_dados)
    
    with t31:
        n=23
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
    with t32:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t33:
        st.write("Relatorios")
        
with tab4:
    t41, t42, t43 = st.tabs(lista_dados)
    
    with t41:
        n=24
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
    with t42:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t43:
        st.write("Relatorios")
        
with tab5:
    t51, t52, t53 = st.tabs(lista_dados)
    
    with t51:
        n=29
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
    with t52:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t53:
        st.write("Relatorios")
        
with tab6:
    t61, t62, t63 = st.tabs(lista_dados)
    
    with t61:
        n=0
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
    with t62:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t63:
        st.write("Relatorios")
        
with tab7:
    t71, t72, t73 = st.tabs(lista_dados)
    
    with t71:
        n=4
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        
        
    with t72:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t73:
        st.write("Relatorios")  
        
with tab8:
    t81, t82, t83 = st.tabs(lista_dados)
    
    with t81:
        #n=29
        #st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        #nro_contrato = f"{df_contratos.iloc[n,1]}"
        df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        st.dataframe(df_selecao)
        
    with t82:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t83:
        
        st.write("Relatorios")              
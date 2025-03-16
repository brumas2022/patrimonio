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
colimage = st.columns((1,1,1))
colimage[1].image("logosanear.png", width=300)

#senha()


lista_contratos=["TECNOBOMBAS - 004/2023", "MASTER - 028/2023", "SPARTACUS", \
                 "MENEGUETI", "GEOPOÇOS", "ALPHA", "SM7", "MASTER - 034/2022", "SAGATEC", "ELETRIC", \
                 "LEILOEIRA", "DA GARISTO", "TECNBOMBAS - 007/2024", "UPX", "GENTE", "RESUMO"]
lista_dados=["Dados", "Medições", "Relatorios"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(lista_contratos)
with tab1:
    
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        
        n=11
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
            
        #open = st.button("Abrir arquivo")
        #if open:
        #    os.startfile('PLANILHA PREGÃO LOTEAMENTOS.pdf')
    with t12:
        n=11
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
        #df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        #st.dataframe(df_selecao)
    with t13:
        st.write("Aqui serão disponibilizados os relatorios mensais de acompanhamento da obra")
        with open("CTR_004-2023_TECNOBOMBAS_BOMBAS_MOTORES_E_SERVICOS_LTDA_assinado.pdf", "rb") as file: 
             st.download_button(label='RELATORIO FEVEREIRO-2025', data=file, file_name="CTR_004-2023_TECNOBOMBAS_BOMBAS_MOTORES_E_SERVICOS_LTDA_assinado.pdf")
      
       
        
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
        st.write("Aqui serão disponibilizados os relatorios mensais de acompanhamento da obra")
        with open("CTR 009-2022 ALPHA CONSTRUTORA EIRELI.pdf", "rb") as file: 
             st.download_button(label='RELATORIO FEVEREIRO-2025', data=file, file_name="CTR 009-2022 ALPHA CONSTRUTORA EIRELI.pdf")
        
with tab7:
    t71, t72, t73 = st.tabs(lista_dados)
    
    with t71:
        n=4
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto", "fiscal"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        
        
    with t72:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t73:
        st.write("Relatorios")  
        
with tab8:
    t81, t82, t83 = st.tabs(lista_dados)
    
    with t81:
        n=13
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        #df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        #st.dataframe(df_selecao)
        
    with t82:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t83:
        
        st.write("Relatorios")
           
with tab9:
        
    t91, t92, t93 = st.tabs(lista_dados)
    
    with t91:
        n=14
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto", "fiscal"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        #df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        #st.dataframe(df_selecao)
        
    with t92:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t93:
        
        st.write("Relatorios") 
        
with tab10:
        
    t101, t102, t103 = st.tabs(lista_dados)
    
    with t101:
        n=19
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        #df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        #st.dataframe(df_selecao)
        
    with t102:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t103:
        
        st.write("Relatorios")
        
with tab11:
        
    t111, t112, t113 = st.tabs(lista_dados)
    
    with t111:
        n=20
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        ##df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        ##st.dataframe(df_selecao)
        
    with t112:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t113:
        
        st.write("Relatorios")
        
with tab12:
        
    t121, t122, t123 = st.tabs(lista_dados)
    
    with t121:
        n=21
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        ##df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        ##st.dataframe(df_selecao)
        
    with t122:
         df_medicao.style.format(hyperlinks="html")
         #st.dataframe(df_medicao.style.format(thousands=".", decimal=","))
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t123:
        
        st.write("Relatorios")             

with tab13:
        
    t131, t132, t133 = st.tabs(lista_dados)
    
    with t131:
        n=22
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        ##df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        ##st.dataframe(df_selecao)
        
    with t132:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t133:
        
        st.write("Relatorios") 
        
with tab14:
        
    t141, t142, t143 = st.tabs(lista_dados)
    
    with t141:
        n=27
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        ##df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        ##st.dataframe(df_selecao)
        
    with t142:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t143:
        
        st.write("Relatorios")      
        
with tab15:
        
    t151, t152, t153 = st.tabs(lista_dados)
    
    with t151:
        n=28
        st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        nro_contrato = f"{df_contratos.iloc[n,1]}"
        ##df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        ##st.dataframe(df_selecao)
        
    with t152:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t153:
        
        st.write("Relatorios")   

with tab16:
        
    t161, t162, t163 = st.tabs(lista_dados)
    
    with t161:
        n=29
        ##st.dataframe(df_contratos.loc[(n, ["contrato", "empresa", "objeto"])])
        ##nro_contrato = f"{df_contratos.iloc[n,1]}"
        df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
        st.dataframe(df_selecao)
        
    with t162:
         st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    with t163:
        
        st.write("Relatorios")         
import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel("RELAÇÃO DE FISCAIS DE CONTRATOS VIGENTES-MEUS.xlsx", sheet_name=0)
df_relacao = df.iloc[3:]
df_relacao.columns = ["CONTRATO", "EMPRESA", "TIPO", "FISCAL CONTRATO", "SUPLENTEFC", "FISCAL OBRA", "SUPLENTEFO", "JAN", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO"]


lista = ["1","2"]
opcao = df_relacao["FISCAL CONTRATO"].unique().tolist()
st.write(opcao)
options = ["MARCOS BRUMATTI", "JAMAL BADIE DAUD", "SINVAL RAIMUNDO DA SILVA", \
           "HERMES ÁVILA DE CASTRO", "DENIZE MARIA SODRÉ DE OLIVEIRA", "GRAZIELA DIAS DEGIACOMETI", \
           "MARIA DA CONCEIÇÃO DE GOIS", "JULIO CESAR SALGADO"]
selection = st.pills("Fiscais de Contrato", opcao)
st.markdown(f"Voce selecionou o seguinte fiscal: {selection}.")

###ESTAVA AQUI
#st.dataframe(df_relacao)

if selection==opcao[0]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[1]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[2]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[3]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[4]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[5]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[6]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[7]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[8]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[9]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[10]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==opcao[11]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
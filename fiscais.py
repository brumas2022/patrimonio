import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel("RELAÇÃO DE FISCAIS DE CONTRATOS VIGENTES.xlsx", sheet_name=0)
lista = ["1","2"]
options = ["MARCOS BRUMATTI", "JAMAL BADIE DAUD", "SINVAL RAIMUNDO DA SILVA", \
           "HERMES ÁVILA DE CASTRO", "DENIZE MARIA SODRÉ DE OLIVEIRA", "GRAZIELA DIAS DEGIACOMETI", \
           "MARIA DA CONCEIÇÃO DE GOIS", "JULIO CESAR SALGADO"]
selection = st.pills("Fiscais de Contrato", options)
st.markdown(f"Voce selecionou o seguinte fiscal: {selection}.")
df_relacao = df.drop([0, 1]) # apaga linhas do dataframe...detalhe nos colchetes
df_relacao.columns = ["GEOBRAS", "CONTRATO", "EMPRESA", "TIPO", "FISCAL CONTRATO", "SUPLENTE1", "FISCAL OBRA", "SUPLENTE"]
#df_nova = df_relacao.

#st.dataframe(df_relacao)

if selection=="MARCOS BRUMATTI":
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[1]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[2]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[3]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[4]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[5]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[6]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
elif selection==options[7]:
    st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']==selection])
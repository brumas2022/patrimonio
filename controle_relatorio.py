import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel("RELAÇÃO DE FISCAIS DE CONTRATOS VIGENTES-MEUS.xlsx", sheet_name=0)
df_relacao = df.iloc[3:]
df_relacao.columns = ["CONTRATO", "EMPRESA", "TIPO", "FISCAL CONTRATO", "SUPLENTEFC", "FISCAL OBRA", "SUPLENTEFO", "JAN", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO"]


st.dataframe(df_relacao[df_relacao['FISCAL CONTRATO']=="MARCOS BRUMATTI"])







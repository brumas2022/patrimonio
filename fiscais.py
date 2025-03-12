import streamlit as st 
import pandas as pd

df = pd.read_excel("RELAÇÃO DE FISCAIS DE CONTRATOS VIGENTES.xlsx", sheet_name=0)

st.dataframe(df)
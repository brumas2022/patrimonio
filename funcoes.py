import pandas as pd
import streamlit as st


df = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=0)

print(df['valor'])

lista = [10, 20, 30, 40, 50]

df1=list(map(lambda x: x*10, df['valor']))

print(df1)

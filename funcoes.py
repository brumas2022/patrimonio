import pandas as pd
import streamlit as st
import streamlit_pdf_viewer as stf

df = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=0)

print(df['valor'])

lista = [10, 20, 30, 40, 50]

df1=list(map(lambda x: x*10, df['valor']))

botao = st.sidebar.button("Arquivo em pdf")

if botao:
    arquivo = stf.pdf_viewer("CTR 009-2022 ALPHA CONSTRUTORA EIRELI.pdf")

    st.write(arquivo)


print(df1)


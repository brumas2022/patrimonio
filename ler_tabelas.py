import pandas as pd
import tabula
import streamlit as st 


tabela = tabula.read_pdf("contratos/arrelatorio_contrato.pdf", pages="all")
df = tabela[0]
st.dataframe(df)
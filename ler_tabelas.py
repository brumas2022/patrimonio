import pandas as pd
import tabula
import streamlit as st 


tabela = tabula.read_pdf("contratos/arrelatorio_contrato.pdf")
df = tabela
st.dataframe(df)
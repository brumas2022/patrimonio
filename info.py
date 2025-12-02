import pandas as pd
import streamlit as st
import os

nome = os.environ("SEGREDO_SANEAR")

st.write(nome)

#df = pd.read_excel("BDTESTES/controle_nad.xlsx")

#st.dataframe(df)
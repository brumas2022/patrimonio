import pandas as pd
import streamlit as st

df = pd.read_excel("BDTESTES/controle_nad.xlsx")

st.dataframe(df)
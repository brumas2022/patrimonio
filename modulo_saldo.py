import streamlit as st
import pandas as pd
df = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=1)

st.dataframe(df)
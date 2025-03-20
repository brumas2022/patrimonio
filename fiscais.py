import streamlit as st 
import pandas as pd

df = pd.read_excel("RELAÇÃO DE FISCAIS DE CONTRATOS VIGENTES.xlsx", sheet_name=0)

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")


if options=="North":
    st.dataframe(df)
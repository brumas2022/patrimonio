import streamlit as st
import pandas as pd 

st.set_page_config("Consulta estoque", layout="wide")

consulta = st.selectbox("Escolha o tipo de consulta", ("POR ITEM", "POR NOME")

                        if consulta=="POR ITEM":
                           st.write("Consulta por item")
                        elif consulta=="POR NOME":
                           st.write("Consulta por nome")


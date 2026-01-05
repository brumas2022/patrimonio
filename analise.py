import pandas as pd
import streamlit as st

st.set_page_config("Controle de analise de projetos", layout="wide")

tabela = pd.read_excel("Controle_de_analise.xlsx", sheet_name=0)

st.dataframe(tabela, hide_index=True, column_config={
        "data_entrada": st.column_config.DatetimeColumn(
            "data_entrada",
            format="DD/MM/YYYY",
            
        ),
        "data_memo": st.column_config.DatetimeColumn(
            "data_memo",
            format="DD/MM/YYYY",
            
        ),
        "data_relatorio": st.column_config.DatetimeColumn(
            "data_relatorio",
            format="DD/MM/YYYY",
            
        ),
        "data_envio": st.column_config.DatetimeColumn(
            "data_envio",
            format="DD/MM/YYYY",
            
        ),
        
        
    })
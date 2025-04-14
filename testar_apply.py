import pandas as pd
import streamlit as st

df = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=0)

#df = df.apply(lambda x: x.strftime("%d/%m/%Y"))
#st.dataframe(df)

st.dataframe(df, hide_index=True, column_config={
        "inicio": st.column_config.DatetimeColumn(
            "inicio",
            format="DD/MM/YYYY",
            
        ),
        "fim": st.column_config.DatetimeColumn(
            "fim",
            format="DD/MM/YYYY",
            
        ),
        "data_portaria": st.column_config.DatetimeColumn(
            "data_portaria",
            format="DD/MM/YYYY",
            
        ),
        "valor": st.column_config.NumberColumn(
            "valor",
            help="nao consegui formatar o valor",
            format="accounting",
            
        ),
    })
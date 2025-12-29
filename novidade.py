import pandas as pd
import streamlit as st

st.set_page_config("Vencimentos de contrato", layout="wide")


def verificar_vencimento():
    aditivos = pd.read_excel("NOVA_MEDICAO.xlsx", sheet_name=1)
    resultado = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=0)
    hoje = pd.Timestamp.now()
    #st.dataframe(resultado)

    #vigencia final
    aditivos['VIGENCIA FINAL'] = pd.to_datetime(aditivos['VIGENCIA FINAL'])
    mascara_vigencia = aditivos['VIGENCIA FINAL'] > hoje
    df_aditivos_vigencia = aditivos[mascara_vigencia]
    st.dataframe(df_aditivos_vigencia)




    resultado['fim'] = pd.to_datetime(resultado['fim'])
    delta_dias = pd.Timedelta(days=90)
    
    tres_meses = pd.Timestamp.now()+delta_dias
    mascara_vencidos = resultado['fim'] > hoje
    df_vencidos = resultado[mascara_vencidos]

    colunas_desejadas = ['contrato', 'empresa', 'objeto', 'fim']
    st.dataframe(df_vencidos[colunas_desejadas], hide_index=True, column_config={
        "fim": st.column_config.DatetimeColumn(
            "fim",
            format="DD/MM/YYYY",
            
        )
    })
    


verificar_vencimento()


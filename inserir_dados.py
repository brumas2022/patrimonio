import streamlit as st
import pandas as pd
import openpyxl

def atualizar(data, atividades):
    workbook = openpyxl.load_workbook("relatorio.xlsx")
    aba = workbook.active
    aba.append([data, atividades])
    workbook.save("reLatorio.xlsx")


lista = ["INSERIR DIARIO DE OBRA", "INSERIR MEDICAO", "INSERIR CONTRATO"]
a = st.sidebar.selectbox("Escolha a opção", lista)

if a==lista[0]:
 
    with st.form("Entrada"):
        data = st.date_input("Data:")
        atividades = st.text_area("Atividades")
        if st.form_submit_button("Confirmar"):
            atualizar(data, atividades)

df = pd.read_excel("relatorio.xlsx")

st.dataframe(df)
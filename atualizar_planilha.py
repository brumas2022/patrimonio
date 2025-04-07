import openpyxl
import streamlit as st
import pandas as pd


def atualizar(data, atividades):
    workbook = openpyxl.load_workbook("relatorio.xlsx")
    aba = workbook.active
    aba.append([data, atividades])
    workbook.save("reLatorio.xlsx")

with st.form("Entrada"):
    data = st.date_input("Data:")
    atividades = st.text_area("Atividades")
    if st.form_submit_button("Confirmar"):
       atualizar(data, atividades)

df = pd.read_excel("relatorio.xlsx")

st.dataframe(df)
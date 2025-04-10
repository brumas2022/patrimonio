import streamlit as st
import pandas as pd
import openpyxl

def atualizar(data, atividades):
    workbook = openpyxl.load_workbook("relatorio.xlsx")
    aba = workbook.active
    aba.append([data, atividades])
    workbook.save("reLatorio.xlsx")
    
def nova_medicao(nro_ctr, nro_medicao, valor, nf, data_nf, data_pagto):
    w_medicao = openpyxl.load_workbook("relatorio.xlsx")
    aba1 = w_medicao.active
    aba1.append([nro_ctr, nro_medicao, valor, nf, data_nf, data_pagto])
    w_medicao.save("novorelatorio.xlsx")


lista = ["INSERIR DIARIO DE OBRA", "INSERIR MEDICAO", "INSERIR CONTRATO"]
a = st.sidebar.selectbox("Escolha a opção", lista)

if a==lista[0]:
 
    with st.form("Entrada"):
        data = st.date_input("Data:")
        atividades = st.text_area("Atividades")
        if st.form_submit_button("Confirmar"):
            atualizar(data, atividades)
elif a==lista[1]:
    with st.form("Medicao"):
        nro_ctr=st.text_input("numero do contrato")
        nro_medicao=st.text_input("Numero medicao")
        valor = st.text_input("valor da medicao")
        nf= st.text_input("Nota fiscal")
        data_nf= st.text_input("DAta da nota")
        data_pagto= st.text_input("Data pagto")
        if st.form_submit_button("Confirmar"):
            nova_medicao(nro_ctr, nro_medicao, valor, nf, data_nf, data_pagto)
        
        
df = pd.read_excel("relatorio.xlsx")

st.dataframe(df)
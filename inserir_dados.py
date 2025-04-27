import streamlit as st
import pandas as pd
import openpyxl

def card():
    st.markdown("<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">", unsafe_allow_html=True)
    st.markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="..." class="card-img-top" alt="...">
                     <div class="card-body">
                          <h5 class="card-title">Card title</h5>
                          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                          <a href="#" class="btn btn-primary">Go somewhere</a>
                     </div>
                </div>)
                """, unsafe_allow_html=True)

def atualizar(data, atividades):
    workbook = openpyxl.load_workbook("relatorio.xlsx")
    aba = workbook["Atividades"]
    aba.append([data, atividades])
    workbook.save("reLatorio.xlsx")
    
def nova_medicao(nro_ctr, nro_medicao, data_medicao, valor, nf, data_nf, data_pagto):
    w_medicao = openpyxl.load_workbook("relatorio.xlsx")
    aba1 = w_medicao["Medicao"]
    aba1.append([nro_ctr, nro_medicao, data_medicao, valor, nf, data_nf, data_pagto])
    w_medicao.save("relatorio.xlsx")


lista = ["INSERIR DIARIO DE OBRA", "INSERIR MEDICAO", "INSERIR CONTRATO", "CARD"]
a = st.sidebar.selectbox("Escolha a opção", lista)

if a==lista[0]:
 
    with st.form("Entrada"):
        data = st.date_input("Data:")
        atividades = st.text_area("Atividades")
        if st.form_submit_button("Confirmar"):
            atualizar(data, atividades)
        df1 = pd.read_excel("relatorio.xlsx", sheet_name=0)  
        st.dataframe(df1)  
    
elif a==lista[1]:
    with st.form("Medicao"):
        nro_ctr=st.text_input("numero do contrato")
        nro_medicao=st.text_input("Numero medicao")
        data_medicao = st.date_input("DAta da medicao")
        valor = st.text_input("valor da medicao")
        nf= st.text_input("Nota fiscal")
        data_nf= st.text_input("DAta da nota")
        data_pagto= st.text_input("Data pagto")
        if st.form_submit_button("Confirmar"):
            nova_medicao(nro_ctr, nro_medicao, data_medicao, valor, nf, data_nf, data_pagto)
    df = pd.read_excel("relatorio.xlsx", sheet_name=1) 
    st.dataframe(df) 
elif a=="CARD":
    card() 
 
        

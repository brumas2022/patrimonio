import streamlit as st
import pandas as pd


# buscar os dados do contrato aqui

import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("URL")
key = os.getenv("KEY")
supabase: Client = create_client(url, key)




df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")
df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=3)
    

df_contratos['selecao'] = df_contratos['contrato']+" - "+ df_contratos['empresa']

df_lista = df_contratos['selecao'].to_list()


a = st.sidebar.selectbox("Escolha", df_lista)

nro = a.split()[0]

st.write(nro)

consulta = supabase.table("bdmedicaonova").select("*").eq("contrato", nro).execute()
consulta1 = supabase.table('dados').select("*").eq("numero", "00000"+nro).execute()


lista_dados = ["Dados", "Medicoes", "Relatorios"]

t11, t12, t13 = st.tabs(lista_dados)

with t11:
    st.write("Em construção")
    st.dataframe(consulta1.data)
    

    contrato = st.text_input("Contrato", placeholder=consulta1.data[0]['numero'])
    medicao_nro = st.text_input("Número da Medição", placeholder=consulta1.data[0]['empresa'])
    #datamedicao = st.text_input("Data da medicao", placeholder=altera.data[a]['datamedicao'])
    #valor = st.text_input("Valor", placeholder=altera.data[a]['valor'])
    #nf = st.text_input("Numero da nota fiscal", placeholder=altera.data[a]['notafiscal'])
    #datanf = st.text_input("Data de Emissao NF", placeholder=altera.data[a]['datanota'])
    #datapgto = st.text_input("Data do pagamento", placeholder=altera.data[a]['datapagto'])
    #observ = st.text_input("Observacao", placeholder=altera.data[a]['observacao'])
    #prot = st.text_input("Protocolo", placeholder=altera.data[a]['protocolo'])
with t12:
    st.dataframe(consulta.data)
with t13:
    st.write("Em construção")

#st.dataframe(consulta.data)


    
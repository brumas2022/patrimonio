import streamlit as st
from datetime import datetime
import pandas as pd

# Entrada de texto
st.write("ENTRADA DE MEDIÇÕES")


# Procurar contrato

df = pd.read_excel("TESTE_MEDICAO.xlsx")

df_nro_contrato = df['CONTRATO'].unique().tolist()

lista = ["ctr 01", "ctr 02"]

nro = st.selectbox("Qual é o contrato? ", df_nro_contrato)

resultado = df.loc[df['CONTRATO']==nro]

# printar as medições deste contrato

st.dataframe(resultado)

# iniciar pelo numero da medicao

col = st.columns((1,1,1))

col[0].write("ETAPA 01")

col[1].write("ETAPA 02")

col[2].write("ETAPA 03")

nro_med = col[0].text_input("entre com o numero da medicao:")

data_med = col[0].date_input("Data da medicao")

valor_med = col[0].text_input("Valor da medicao")

nf = col[1].text_input("Numero da nf")

data_nf = col[1].date_input("Data da NF")

data_pagto = col[1].date_input("Data do pagamento")

observacao  = col[2].text_input("Observacao")

protocolo = col[2].text_input("Numero do protocolo")




# Seleção de número
idade = st.slider("Selecione sua idade:", 0, 100, 25)
st.write(f"Sua idade é: {idade}")

# Checkbox
aceita_termos = st.checkbox("Aceito os termos e condições")
if aceita_termos:
    st.write("Você aceitou os termos.")

# Upload de arquivo
arquivo_carregado = st.file_uploader("Carregue um arquivo CSV:")
if arquivo_carregado:
    st.write("Arquivo carregado com sucesso!")
    # Para processar o arquivo, você pode usar a biblioteca pandas:
    # import pandas as pd
    # df = pd.read_csv(arquivo_carregado)
    # st.dataframe(df)

# Botão de envio
if st.button("Enviar"):
    st.write("Formulário enviado!")
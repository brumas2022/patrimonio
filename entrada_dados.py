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

df_editado = st.data_editor(resultado)



if st.button("CONFIRMA EDICAO ?"):
   # aqui eu preciso voltar ao df original

   
   df_editado.to_excel("TESTE_MEDICAO.xlsx", index=False)



st.write("---")

# iniciar pelo numero da medicao

col = st.columns((1,1,1))

col[0].write("DADOS DA MEDICAO")

col[1].write("DADOS DO PAGAMENTO")

col[2].write("OUTROS")

nro_med = col[0].text_input("entre com o numero da medicao:")

data_med = col[0].text_input("Data da medicao")

valor_med = col[0].text_input("Valor da medicao")

nf = col[1].text_input("Numero da nf")

data_nf = col[1].text_input("Data da NF")

data_pagto = col[1].text_input("Data do pagamento")

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
    dado_novo = {
        "CONTRATO": [nro],
        "NRO MEDICAO": [nro_med],
        "DATA MEDICAO":[data_med],
        "VALOR":[valor_med],
        "NF": [nf],
        "DATA NF":[data_nf],
        "DATA PAGTO":[data_pagto],
        "OBSERVACAO":[observacao],
        "protocolo":[protocolo]
    }
    df_inserido = pd.DataFrame(dado_novo)
    st.dataframe(df_inserido)
    df_combined = pd.concat([df, df_inserido], ignore_index=True)
    #st.dataframe(df_combined)
    df_combined.to_excel("TESTE_MEDICAO.xlsx", index=False)
    #st.rerun()
    st.write("Formulário enviado!")
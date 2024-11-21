import streamlit as st
import pandas as pd

st.title("Consulta do estoque")

form = st.form(key="Clientes", clear_on_submit=True)
paises = ['Brasil', 'Italia']

df=pd.read_excel("Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
nomes_orc = df['Item'].tolist()
with form:
    st.selectbox("Escolha o item", nomes_orc) 
    #input_name = st.text_input("Nome")
    #input_email = st.text_input("Email")
    #input_password = st.text_input("Senha", type="password")
    #input_pais = st.selectbox("Selecione pais ", paises)
    
    botao_submit = form.form_submit_button("Confirma!")
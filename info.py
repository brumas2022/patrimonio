import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv


# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()
# Acessando a variável de ambiente API_KEY
#CHAVE_API = os.getenv("CHAVE_API")
nome = os.getenv("senha")

st.write(nome)

#df = pd.read_excel("BDTESTES/controle_nad.xlsx")

#st.dataframe(df)

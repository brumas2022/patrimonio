import streamlit as st
import pandas
import requests
import pprint

#api_key=
link_api="https://api.adviceslip.com/advice"

resposta = requests.get(link_api)

print(resposta)
print(resposta.content)
dados_requisicao = resposta.json()
pprint.pprint(dados_requisicao)
conselho = dados_requisicao['slip']['advice']
st.write(conselho)
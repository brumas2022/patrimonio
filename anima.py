import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#link outro
b = "https://lottie.host/734268e3-0c30-466d-9788-b2a199859f51/TfB8MvN808.json"


# Link de um bonequinho (exemplo)
a = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"

lottie_hello = load_lottieurl(b)

col1, col2 = st.columns([1, 3])

with col1:
    st_lottie(lottie_hello, speed=1, height=200, key="initial")

with col2:
    st.write("### Olá! Eu sou o seu assistente.")
    st.info("Aqui estão as informações que você precisa para hoje...")
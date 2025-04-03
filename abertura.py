import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config("Pagina Diretoria")
st.image("img.png")

with open('style1.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col=st.columns((1,1))
a = col[0].button("CONTRATOS", use_container_width=True)
b = col[0].button("FISCAIS", use_container_width=True)
c = col[0].button("ESTRUTURA SANEAR", use_container_width=True)

d = col[1].button("ANDAMENTO DAS OBRAS", use_container_width=True)
e = col[1].button("CONTROLE ESTOQUE", use_container_width=True)
f = col[1].button("PLANEJAMENTO ESTRATEGICO", use_container_width=True)

if d:
   
   webbrowser.open_new("http://obras-contrato.streamlit.app") 
if e:
   webbrowser.open_new_tab("http://estoque1.streamlit.app")
if a:
   st.header("DEu certo")



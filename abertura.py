import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config("Pagina Diretoria")
st.image("contratos/Logosanear1.jpg")

with open('style1.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col=st.columns((1,1))
a = col[0].link_button("CONTRATOS", "http://obras1.streamlit.app", use_container_width=True)
b = col[0].link_button("FISCAIS", "https://fiscais.streamlit.app/", use_container_width=True)
c = col[0].link_button("ESTRUTURA SANEAR", "https://estrutura1.streamlit.app", use_container_width=True)

d = col[1].link_button("ANDAMENTO DAS OBRAS", "http://obras2.streamlit.app", use_container_width=True)
e = col[1].link_button("CONTROLE ESTOQUE", "http://estoque1.streamlit.app", use_container_width=True)
f = col[1].link_button("PLANEJAMENTO ESTRATEGICO", "https://comunicasanear-avcnrpqesbpzeg2ecsmuun.streamlit.app",  use_container_width=True)

#col[2].link_button("teste1", "http://obras2.streamlit.app", use_container_width=True)
#col[2].link_button("teste2", "http://obras2.streamlit.app", use_container_width=True)
#col[2].link_button("teste3", "http://obras2.streamlit.app", use_container_width=True)

if d:
   webbrowser.open("http://obras-contrato.streamlit.app") 
if e:
   webbrowser.open_new_tab("http://estoque1.streamlit.app")
if a:
   pass




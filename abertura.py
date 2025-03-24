import streamlit as st
import pandas as pd

st.set_page_config("Pagina Diretoria")
st.image("img.png")

with open('style1.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col=st.columns((1,1))
col[0].button("CONTRATOS", use_container_width=True)
col[0].button("FISCAIS", use_container_width=True)
col[0].button("ESTRUTURA SANEAR", use_container_width=True)

col[1].button("ANDAMENTO DAS OBRAS", use_container_width=True)
col[1].button("CONTROLE ESTOQUE", use_container_width=True)



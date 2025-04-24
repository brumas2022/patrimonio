import streamlit as st
import pandas as pd

lista_engenheiros = ["Fabiola", "Wilma", "Joao Couto", "Erika", "Jamal", "Rudiny", "Hermes", "Dalton", "Denize", "Joao Manoel", "Alberto"]

choice = st.sidebar.selectbox("Escolha o engenheiro", lista_engenheiros)

if choice == lista_engenheiros[0]:
    st.write("Especialidade : Civil")
    st.write("Projetos em andamento")
    

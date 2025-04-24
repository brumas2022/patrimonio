import streamlit as st
import pandas as pd

lista_engenheiros = ["Fabiola", "Wilma", "Joao Couto", "Erika", "Jamal", "Rudiny", "Hermes", "Dalton", "Denize", "Joao Manoel", "Alberto"]
df = pd.read_csv("eng.csv")
lista = df["Nome"].tolist()

choice = st.sidebar.selectbox("Escolha o engenheiro", lista)


resultado_item = df[df['Nome']==choice]


if choice == lista_engenheiros[0]:
    st.dataframe(resultado_item, hide_index=True)
elif choice == lista_engenheiros[1]:
    st.dataframe(resultado_item, hide_index=True)
elif choice == lista_engenheiros[2]:
    st.dataframe(resultado_item, hide_index=True)    
elif choice == lista_engenheiros[3]:
    st.dataframe(resultado_item, hide_index=True)
elif choice == lista_engenheiros[4]:
    st.dataframe(resultado_item, hide_index=True)
elif choice == lista_engenheiros[5]:
    st.dataframe(resultado_item, hide_index=True)
elif choice == lista_engenheiros[6]:
    st.dataframe(resultado_item, hide_index=True) 
elif choice == lista_engenheiros[7]:
    st.dataframe(resultado_item, hide_index=True) 
elif choice == lista_engenheiros[8]:
    st.dataframe(resultado_item, hide_index=True) 
elif choice == lista_engenheiros[9]:
    st.dataframe(resultado_item, hide_index=True) 
elif choice == lista_engenheiros[10]:
    st.dataframe(resultado_item, hide_index=True)     
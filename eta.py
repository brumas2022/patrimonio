import streamlit as st

a = st.sidebar.button("PROJETOS")
b = st.sidebar.button("LICITACAO")

if a:
    c = st.selectbox("QUAL PROJETO", ("FLOCULADOR", "DECANTADOR"))
    
    if c=="FLOCULADOR":
       st.write("Este é o projeto do floculador") 

        
                     

import streamlit as st

a = st.sidebar.button("PROJETOS")
b = st.sidebar.button("LICITACAO")
c = st.sidebar.button("OBRA")
d = st.sidebar.button("PENDENCIAS DA OBRA")
e = st.sidebar.button("PENDENCIAS DA ETA 2")

if a:
    c = st.selectbox("QUAL PROJETO", ("FLOCULADOR", "DECANTADOR"))
    
    if c=="FLOCULADOR":
       st.write("Este é o projeto do floculador") 
    
    if c=="DECANTADOR":
        st.write("ESTE É O PRJETO DECANTADOR")
        with open("CTR 009-2022 ALPHA CONSTRUTORA EIRELI.pdf", "r") as f:
            arquivo = f.read()
            st.markdown(arquivo)

        
                     

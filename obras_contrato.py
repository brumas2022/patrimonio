import streamlit as st 

lista_contratos=["TECNOBOMBAS", "MASTER", "SPARTACUS"]
lista_dados=["Dados", "Medições", "Relatorios"]
tab1, tab2, teab3 = st.tabs(lista_contratos)
with tab1:
    
    t11, t12, t13 = st.tabs(lista_dados)
    with t11:
        st.write("Contrado Nro")
    with t12:
        st.write("Medição nro")
    with t13:
        st.write("Relatorio")
        
with tab2:
    t21, t22, t23 = st.tabs(lista_dados) 
    
    with t21:
        st.write("Contrado Nro")
    with t22:
        st.write("Medição nro")
    with t23:
        st.write("Relatorio")
        
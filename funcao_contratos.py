import streamlit as st
def grafico(a,b):
    resultado = a*b
    return resultado

def relatorio(x):
    
    st.dataframe(x)
    return 

def senha():
    
    form = st.form(key="Obras", clear_on_submit=True)
    with form:
        lista = ["marcos", "maria", "pitoca"]
        email = st.text_input("Qual o seu nome")
        a=st.text_input("Entre com a senha", type="password" )
        b="102030"
        botao_submit = form.form_submit_button("Confirma!")
        if a==b and email in lista:
            st.write(f"{email}, acesso liberado!!!")
            word=True
            #st.dataframe(df.iloc[3:], hide_index=True)
        if a!="":
             st.write(f"{email}, a senha está incorreta. Verifique como desenvolvedor do produto")
    return word
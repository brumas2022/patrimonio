import streamlit as st
import pandas as pd
#from openpyxl import load_workbook

st.set_page_config("Sessão de dados", layout="wide")

with st.form("Cadastro"):
    dia = st.date_input("Dia do mês")
    anotacao = st.text_area("Descrição da atividade")
    pessoa = st.text_input("Pessoas envovidas")
    
    if st.form_submit_button():
        if 'data' not in st.session_state:
            st.session_state.data = pd.DataFrame(columns=['dia', 'anotacao', 'pessoa'])
        dados = {'dia': dia, 'anotacao': anotacao, 'pessoa': pessoa}
        df = pd.DataFrame(dados, index=[0])
        st.session_state.data = pd.concat([st.session_state.data, df], ignore_index=True)
        #wb = load_workbook("teste_outro.xlsx", read_only=False)

        #ws = wb.active
        #ws.append(st.session_state.data)
        #wb.save("teste_outro.xlsx")
        #st.rerun()
        
        
        st.success("Dados inseridos com sucesso")
    
st.write("Lista")
if 'data' in st.session_state:
    st.write(st.session_state.data)


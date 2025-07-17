import streamlit as st
import pandas as pd

st.set_page_config("Materiais licitados", layout="wide")

def medicao():
   #st.header("Controle do PREGAO 013/2024")
   #def highlight_survived1(s):
   # return ['background-color: darkorange']*len(s) if s['SITUACAO'] == 'AGUARDANDO ENTREGA' else ['background-color: lightgrey']*len(s)
   
   st.info("CAPTAÇÃO DE AGUA BRUTA, ELEVATORIA RC1, ELEVATORIA RC2 E UFMT")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=0)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA EMVIO NAD", "SITUACAO", "PRAZO DE ENTREGA", "DIAS", "OBSERVACAO"]
   
   ##"LOTE", "EMPRESA", "VALOR", "DATA EMVIO NAD", "SITUACAO", "PRAZO DE ENTREGA", "DIAS", "OBSERVACAO"
   st.dataframe(df_medicao.iloc[3:16], hide_index=True)
   st.markdown(":red[***Ultima atualização em 06/03/2025 - V E GOMES entregou ultima peça, um TUBO FERRO FUNDIDO, FLANGE/FLANGE - PN 10 - DN 700MM - L=0,5]")
   st.markdown(":green[***Ultima atualização em 12/03/2025 - TAF ENTREGOU LOTE PARAFUSOS 125.899,9]")
   st.markdown(":red[***Ultima atualização em 13/03/2025 - TUBCON ENTREGOU 258.900,56 - restante do LOTE 01, lote 03 completo e restante do lote 04]")
   
def medicao1():
   #st.header("Controle do PREGAO 014/2024")
   st.info("LOTEAMENTOS CPA, MARIA AMELIA, ALTAMIRANDO II E ALFREDO III")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=1)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2", "SITUACAO 2"]
   
   
   st.dataframe(df_medicao.iloc[3:16], hide_index=True)
   st.markdown(":red[***Ultima atualização em 06/03/2025 - CONSTRUFER entregou TOTAL DA NAD2 no valor de 6.313,03]")
   st.markdown(":green[***Ultima atualização em 10/03/2025 - CORR PLASTIK emitiu NF no total de 52.972,90]")
   st.markdown(":red[***Ultima atualização em 11/03/2025 - ENGESAN entregou o lote completo]")
   
def medicao2():
   #st.header("Controle do PREGAO 014/2024")
   st.info("AMPLIAÇÃO DO SISTEMA DE ABASTECIMETNO DE ÁGUA NA ESTAÇÃO DE TRATAMENTO DE ÁGUA (ETA)")
   
   df_medicao = pd.read_excel("PREGAO 13.xlsx", sheet_name=2)
   df_medicao.columns=["LOTE", "EMPRESA", "VALOR", "DATA NAD1", "VALOR NAD1", "SITUAÇAO", "DATA NAD2", "VALOR NAD2"]
   
   #st.dataframe(df_medicao, hide_index=True, column_config={
   #     "DATA NAD1": st.column_config.DatetimeColumn(
   #         "DATA NAD1",
   #         format="D MM YYYY",
   #         
   #     ),
   # })
   
   
   st.dataframe(df_medicao.iloc[3:8], hide_index=True)
   st.markdown(":green[Em 19/03/2025 - Chegou Registro de gaveta DN 600]")
   with open("PREGAO 13.xlsx", "rb") as file: 
      st.download_button(label='PLANILHA ORIGINAL', data=file, file_name="PREGAO 13.xlsx") 
      
         
def estoque_zero():
   ##entrar()
   st.info("As informações desta seção refere-se ao banco de dados da Coplan com todos os itens zerados no estoque")
   df_zero=pd.read_excel("Zero_Estoque_Data_Atual_Excel.xlsx", sheet_name=0)
   df_zero.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   item_zero=df_zero["Item"].tolist()
   z = st.selectbox("Escolhao item", item_zero)
   resultado_item_zero=df_zero[df_zero["Item"]==z]
   st.dataframe(resultado_item_zero, hide_index=True)
   st.write("Data e horario da atualização : ", df_zero.columns[1]) 
   
   
st.sidebar.header("Materiais e equipamentos das obras")

a = st.sidebar.button("PREGAO 012/2024", use_container_width=True)
b = st.sidebar.button("PREGAO 013/2024", use_container_width=True)
c = st.sidebar.button("PREGAO 014/2024", use_container_width=True)

if a:
    medicao2()
elif b:
    medicao()
elif c:
    medicao1()
else:
    st.header("Materiais e equipamentos para obras")
    st.image("contratos/Logosanear1.jpg")


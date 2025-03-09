import streamlit as st 
from openpyxl import load_workbook

wb = load_workbook("teste_outro.xlsx", read_only=False)

ws = wb.active

nome = st.text_input("Qual o seu nome? ")
dia_nasc = st.text_input("Qual o dia do seu nascimento? ")
idade = st.text_input("Qautnos anos vc tem?")

a=st.button("Confirme")
if a:
    ws.append([nome, dia_nasc, idade])
    wb.save("nova.xlsx")

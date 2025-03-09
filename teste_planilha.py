import streamlit as st 
from openpyxl import load_workbook

wb = load_workbook("teste_outro.xlsx", read_only=False)

ws = wb.active

ws.append(["mara", "06", "55"])
wb.save("nova.xlsx")

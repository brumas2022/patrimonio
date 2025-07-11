import streamlit as st
import pandas as pd
import openpyxl

df = pd.excel("NOVA_MEDICAO.xlsx", sheet_name=0)

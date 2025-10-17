import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

# Carregar a planilha Excel
file_path = 'caminho/para/sua/planilha.xlsx'  # Substitua pelo caminho da sua planilha
sheet_name = 'Nome_da_Aba'  # Substitua pelo nome da aba que contém os dados

# Ler a planilha
df = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=0)

# Supondo que a coluna de data se chama 'Data'
# Certifique-se de que o nome da coluna está correto
df['fim'] = pd.to_datetime(df['fim'])

# Data atual
data_atual = datetime.now()

# Calcular a data limite (60 dias a partir de hoje)
data_limite = data_atual + timedelta(days=60)

# Filtrar as linhas que faltam 60 dias para vencer
linhas_faltando = df[(df['fim'] > data_atual) & (df['fim'] <= data_limite)]

# Exibir as linhas filtradas
print(linhas_faltando)
st.dataframe(linhas_faltando)
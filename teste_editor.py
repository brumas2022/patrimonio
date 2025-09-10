import streamlit as st
import pandas as pd

# 1. Crie um DataFrame original
df_original = pd.DataFrame({
    "Produto": ["Maçã", "Banana", "Laranja"],
    "Quantidade": [100, 150, 120]
})

# 2. Exiba o editor de dados
st.header("Edite os dados da sua tabela")
df_editado = st.data_editor(df_original, num_rows="dynamic") # num_rows="dynamic" permite adicionar novas linhas

# 3. Adicione um botão para gravar os dados
if st.button("Salvar alterações"):
    # O df_editado agora contém os dados mais recentes do editor
    df_editado.to_csv("dados_editados.csv", index=False)
    st.success("Dados salvos em 'dados_editados.csv'!")
else:
    st.info("Clique no botão para salvar os dados")
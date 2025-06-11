import pandas as pd
import tabula
import streamlit as st
import tkinter as tk
from tkinter import filedialog
 



tabela = tabula.read_pdf("contratos/arrelatorio_contrato.pdf")
df = tabela
#st.dataframe(df)

def salvar_arquivo():
    """
    Abre uma caixa de diálogo para o usuário escolher um local para salvar o arquivo.
    """
    # Define o título e o tipo de diálogo
    file_path = filedialog.asksaveasfilename(
        title="Escolha o Local para Salvar o Arquivo",
        defaultextension=".txt",  # Extensão padrão (opcional)
        filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")]
    )

    # Verifica se o usuário escolheu um local
    if file_path:
        print("Caminho do arquivo selecionado:", file_path)
        # Aqui você pode usar o file_path para salvar o arquivo
        # Por exemplo, para abrir o arquivo em modo de escrita:
        # with open(file_path, 'w') as f:
        #    f.write("Conteúdo do arquivo")


# Cria a janela principal (opcional, mas útil para um aplicativo)


# Cria um botão para abrir a caixa de diálogo
#botao = st.button()
botao = st.button(label="Escolher Local para Salvar", on_click=salvar_arquivo)


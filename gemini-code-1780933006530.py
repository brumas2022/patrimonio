import customtkinter as ctk
import sqlite3
import pandas as pd
from fpdf import FPDF

# Configuração Visual
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SANEAR - Gestão de Contratos (TCE-MT)")
        self.geometry("600x500")

        # Botão para Importar Excel
        self.btn_import = ctk.CTkButton(self, text="Importar Planilha de Contratos", command=self.importar_excel)
        self.btn_import.pack(pady=20)
        
        # Campo para Ocorrência (Exemplo)
        self.txt_ocorrencia = ctk.CTkTextbox(self, width=500, height=150)
        self.txt_ocorrencia.pack(pady=10)
        
        # Botão para PDF
        self.btn_pdf = ctk.CTkButton(self, text="Gerar Relatório Mensal PDF", command=self.gerar_relatorio)
        self.btn_pdf.pack(pady=20)

    def importar_excel(self):
        # Lógica para ler Excel e salvar no SQLite
        pass

    def gerar_relatorio(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Relatório Mensal de Acompanhamento - TCE-MT", ln=True, align='C')
        # Aqui você mapeia os campos do seu PDF original (CTR 011-2023)
        pdf.output("relatorio_mensal.pdf")
        print("PDF Gerado com sucesso!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
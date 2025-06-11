import streamlit as st 
from fpdf import FPDF


def imprime():
    pdf = FPDF("P", "mm", "A4") 
    pdf.add_page() 
    pdf.set_font("Arial" , size=10) 
    #pdf.cell(200, 10, txt = "Bem-vindo ao Python!", ln = 1, align="C")
    #      pdf.cell(100, 50, txt="Novo texto....avante" )
    #pdf.cell()"C:/Users/Compras/Documents/GitHub/patrimonio/
    #pdf.image("img.png", x=60, y=10, w=90, h=20) 
    pdf.text(50, 40, txt="RELATORIO MENSAL DE ACOMPANHAMENTO DE CONTRATO")
    relatorio = pdf.output("meupdf.pdf", dest="")
    caminho = "c:\ProjetosPY"
    st.download_button("Download", relatorio, caminho)
    #pdf.output("meupdf.pdf", dest="")
     
    
    return

imprime()


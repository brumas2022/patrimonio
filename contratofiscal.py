import pandas as pd
import streamlit as st
#from streamlit_extras.colored_header import colored_header
#from streamlit_extras.add_vertical_space import add_vertical_space
import psycopg2

#from reportlab.pdfgen import canvas  # impressap de pdf
import fpdf
from fpdf import FPDF

st.set_page_config(page_title="Contratos do fiscal Marcos Brumatti", layout="wide", menu_items={'About':"Its very cool"})


pdf = FPDF("P", "mm", "A4") 
pdf.add_page() 
pdf.set_font("Arial" , size=12) 
#pdf.cell(200, 10, txt = "Bem-vindo ao Python!", ln = 1, align="C")
#pdf.cell(100, 50, txt="Novo texto....avante" )
#pdf.cell()
pdf.image("C:/Users/Compras/Documents/GitHub/patrimonio/img.png", x=50, y=10, w=100, h=20) 
pdf.cell(0, 7, txt="RELATORIO MENSAL DE ACOMPANHAMENTO DE CONTRATO", ln=1, border=1, align="C")
pdf.rect(10, 80, 500, 90)
pdf.cell(10, 80, txt="CONTRATO N°")
pdf.cell(10, 100, txt="EMPRESA")
pdf.cell(10, 120, txt="OBJETO")
pdf.cell(10, 150, txt="VIGENCIA")
pdf.cell(10, 170, txt="VALOR")
pdf.cell(10, 190, txt="LICITACAO")
pdf.output("simple_demo.pdf")
pdf.write("deu certo")


def imprime():
    resultado = ['teste1', 'teste2', 'teste3', 'teste4', 'teste5', 'teste6']
    
    
    with st.form(key="realtorioempdf"):
          relatbutton=st.form_submit_button()
          if relatbutton:
               cnv = canvas.Canvas("relatorio.pdf")
               cnv.drawImage("img.png", 200, 800, width=200, height=40)
               #cnv.circle(100, 100, 30)
               #cnv.line(100, 100, 200, 100)
               acesso = resultado[5].strftime("%d/%m/%Y")

               teste_split = resultado[3].rsplit(None, 16)
               resu = str(teste_split[0])
               print(teste_split)
               print(resu)
               print(acesso)
               print(resultado[5])

               cnv.setFont("Helvetica-Bold", 10)
               cnv.drawString(150,770,"RELATORIO MENSAL DE ACOMPANHAMENTO DE CONTRATO")
               cnv.setFont("Helvetica", 10)
               cnv.drawString(60, 740, "CONTRATO N° :  "+resultado[1]+"/"+resultado[2])
               cnv.drawString(350, 740, "DATA DE ABERTURA : "+acesso)
               cnv.drawString(55, 710, "CONTRATADO(A)  :  "+resultado[4])
               cnv.drawString(55, 690, "TERMO DO CONTRATO  ")
               cnv.drawString(205, 690, resu)

               cnv.drawString(55, 600, "UNIDADE DETENTORA DO CONTRATO")
               cnv.drawString(55, 580, "DATA DO INICIO : "+ acesso)
               cnv.drawString(250, 580, "VALOR DO CONTRATO  "+resultado[10])
               cnv.drawString(55, 560, "DATA DA CONCLUSAO")
               cnv.drawString(250, 560, "LICITACAO")
               cnv.drawString(55, 540, "PRAZO DO CONTRATO")
               cnv.drawString(250, 540, "RECURSO")
               cnv.rect(50,615, 500, 90)
               cnv.rect(50, 535, 500, 55 )




               cnv.drawString(55, 520, "Ocorrencias")
               cnv.drawString(160, 520, resultado1[3])

               cnv.drawString(55,430, "Diligiencias")
               cnv.drawString(55, 415, "demandadas e")
               cnv.drawString(55, 400, "providencias")
               cnv.drawString(55, 385, "adotadas")
               cnv.drawString(160,430, resultado1[4])


               cnv.drawString(55, 350, "Avaliação dos")
               cnv.drawString(55, 335, "serviços e")
               cnv.drawString(55, 320,"documentos")
               cnv.drawString(55, 305, "apresentados")
               cnv.drawString(55, 290, "pela empresa")
               cnv.drawString(160, 350, resultado1[5])


               cnv.drawString(55, 270, "Observações/")
               cnv.drawString(55, 255, "Seguestões/")
               cnv.drawString(55, 240, "Reclamações")
               cnv.drawString(160, 270, resultado1[6])

               print(cnv.getAvailableFonts())

               # ultimo retangulo da assinatura
               cnv.rect(50, 30, 500, 60)
               cnv.line(50, 50, 350, 50)  ##aqui vai a palavra ASSINATURA
               cnv.line(50, 70, 550, 70)
               cnv.line(350, 30, 350, 90)



               cnv.rect(50, 200, 100, 330)
               cnv.rect(150, 200, 400, 330)
               cnv.line(50, 282, 550,282 )
               cnv.line(50, 364,550, 364)
               cnv.line(50, 446, 550, 446)
               cnv.rect(50, 100, 500, 90)

               cnv.drawString(400, 80, "ASSINATURA")
               cnv.drawString(55, 80, 'FISCAL DE CONTRATOS : '+ 'MARCOS BRUMATTI')
               cnv.drawString(55, 60, "PORTARIA N° "+'056/2022')
               cnv.drawString(55, 40, "RELATORIO REFERENTE A :  "+resultado1[7].strftime('%d/%m/%y'))

               #cnv.drawString(150, 740, "034/2022")
               cnv.showPage()
               cnv.save()
               webbrowser.open("relatorio.pdf")


#imprime()
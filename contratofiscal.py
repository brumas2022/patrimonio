import pandas as pd
import streamlit as st
#from streamlit_extras.colored_header import colored_header
#from streamlit_extras.add_vertical_space import add_vertical_space
import psycopg2

#from reportlab.pdfgen import canvas  # impressap de pdf
import fpdf
from fpdf import FPDF



st.set_page_config(page_title="Contratos do fiscal Marcos Brumatti", layout="wide", menu_items={'About':"Its very cool"})

df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")

df_aditivos = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=1)

df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=2)

col = st.columns((1,1,1,1))
#n=18
# nro_indice = st.selectbox("Escolha o  contrato", ("1", "2", "3"))

enviar = col[2].button("EMITE RELATORIO")
mostrar = col[2].button("MOSTRA MEDICAO")

nro = col[0].number_input("Digite um nro", format="%i")
n = int(nro)
nro_contrato = col[0].text_input("CONTRATO/ANO", value=f"{df_contratos.iloc[n,1]}")
empresa = col[0].text_input("EMPRESA", value=f"{df_contratos.iloc[n,2]}")
objeto = col[0].text_input("OBJETO", value=f"{df_contratos.iloc[n,3]}")
valor = col[0].text_input("VALOR", value=f"{df_contratos.iloc[n,7]}")
data_inicio = col[0].text_input("DATA INICIAL", value=f"{df_contratos.iloc[n,4].strftime("%d/%m/%Y")}")
data_fim = col[0].text_input("DATA FINAL", value=f"{df_contratos.iloc[n,5].strftime("%d/%m/%Y")}")

data_aditivo = col[2].text_input("ULTIMO ADITIVO", value=f"{df_aditivos.iloc[n,3].strftime("%d/%m/%Y")}")

licitacao = col[0].text_input("LICITACAO N°/ANO", value=f"{df_contratos.iloc[n,8]}")

portaria_nro = col[1].text_input("Numero da portaria", value=f"{df_contratos.iloc[n,11]}")
portaria_data = col[1].text_input("Data portaria", value=f"{df_contratos.iloc[n,12].strftime("%d/%m/%Y")}")

ordem_inicio = col[2].text_input("Data da ordem de inicio", value= f"{df_contratos.iloc[n,14]}")

obs = col[1].text_input("Observação")
diligencia = col[1].text_input("Diligencias")
ocorrecias = col[1].text_input("Ocorrencias")
data_relatorio = col[1].date_input("Data do relatorio")
data_relatorio_1 = data_relatorio.strftime("%d/%m/%Y")
st.dataframe(df_contratos)
## st.write(tecla) ##quero clicar no dataframe e ele atribuir o valor do click para abrir outra janela

if mostrar:
    st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    df_selecao=df_medicao.groupby(by='CONTRATO').sum(numeric_only=True)
    st.dataframe(df_selecao)
    #st.write(df_medicao.loc["VALOR"].sum(["CONTRATO"]=="028/2023"))
if enviar:
    #st.dataframe(df_medicao[df_medicao["CONTRATO"]==nro_contrato])
    
    pdf = FPDF("P", "mm", "A4") 
    pdf.add_page() 
    pdf.set_font("Arial" , size=10) 
    #pdf.cell(200, 10, txt = "Bem-vindo ao Python!", ln = 1, align="C")
    #      pdf.cell(100, 50, txt="Novo texto....avante" )
    #pdf.cell()
    pdf.image("C:/Users/Compras/Documents/GitHub/patrimonio/img.png", x=60, y=10, w=90, h=20) 
    pdf.text(50, 40, txt="RELATORIO MENSAL DE ACOMPANHAMENTO DE CONTRATO")
    #pdf.rect(x=10, y=70, w=180, h=8)
    #pdf.rect(x=10, y=70, w=60, h=8)
    #
    # pdf.rect(x=70, y=70, w=60, h=8)
    pdf.text(11, 50, txt="CONTRATO N° : "+nro_contrato)
    pdf.text(130, 50, txt="DATA DE ABERTURA: "+data_inicio)
    pdf.text(11, 60, txt="CONTRATADO(A)")
    pdf.text(51, 60, empresa)
    pdf.rect(10, 55, 40, 10)
    pdf.rect(50, 55, 150, 10)
    pdf.text(11, 73, txt="TERMO DO CONTRATO : ")
    pdf.text(53, 73, txt=objeto[:65])
    pdf.text(53, 78, txt=objeto[65:130])
    pdf.text(53, 83, txt=objeto[130:195])
    
    pdf.rect(10, 68, 190, 20)
    pdf.text(11, 95, txt="UNIDADE DETENTORA DO CONTRATO:")
    pdf.rect(10, 90, 190, 8)
    pdf.rect(10, 98, 190, 20)
    pdf.text(11, 105, txt="DATA DO INICIO : "+data_inicio)
    pdf.text(11, 110, txt="DATA DA CONCLUSAO : "+data_fim)
    pdf.text(11, 115, txt="PRAZO DO CONTRATO : 365 DIAS")
    pdf.text(121, 105, txt="VALOR DO CONTRATO : "+valor)
    pdf.text(121, 110, txt="LICITACAO : "+licitacao)
    pdf.text(121, 115, txt="RECURSO : PROPRIO")
    pdf.rect(10, 120, 30, 30)
    pdf.rect(10, 150, 30, 30)
    pdf.rect(10, 180, 30, 30)
    pdf.rect(10, 210, 30, 30)
    pdf.text(11, 125, txt="Ocorrencias")
    pdf.text(51, 125, txt=ocorrecias)  #texto da ocorrencia

    pdf.text(11, 155, txt="Diligencias")
    pdf.text(51, 155, txt=diligencia) # texto da diligencia
    pdf.text(11, 160, txt="demandas e")
    pdf.text(11, 165, txt="providências")
    pdf.text(11, 170, txt="adotadas")

    pdf.text(11, 185, txt="Avaliação dos")
    pdf.text(51, 185, txt="Serviço efetuado conforme contratado.") # texto da avaliação
    pdf.text(11, 190, txt="serviços e")
    pdf.text(11, 195, txt="documentos")
    pdf.text(11, 200, txt="apresentados")
    pdf.text(11, 205, txt="pela empresa")

    pdf.text(11, 215, txt="Observacoes /")
    pdf.text(51, 215, txt=obs)  # texto da observação
    pdf.text(11, 220, txt="Sugestões /")
    pdf.text(11, 225, txt="Reclamações")

    pdf.rect(40, 120, 160, 30)
    pdf.rect(40, 150, 160, 30)
    pdf.rect(40, 180, 160, 30)
    pdf.rect(40, 210, 160, 30)

    pdf.rect(10, 260, 100, 8)
    pdf.text(11, 265, txt="FISCAL DE CONTRATO : MARCOS BRUMATTI")
    pdf.rect(10, 268, 100, 8)
    pdf.text(11, 273, txt=f"PORTARIA N° {portaria_nro},"+f"DATA: {portaria_data}")
    pdf.rect(10, 276, 100, 8)
    pdf.text(11, 281, txt=f"RELATORIO REFERENTE A : {data_relatorio_1}")

    pdf.rect(110, 260, 90, 8)
    pdf.text(130, 265, txt='ASSINATURA')
    pdf.rect(110, 268, 90, 16)


    
    pdf.output(f"C:/Users/Compras/Desktop/2024/fiscaldecontratos/CTR {nro_contrato.replace("/", "-")} {empresa}.pdf")
    


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
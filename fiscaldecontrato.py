import pandas as pd
import streamlit as st
#import fpdf
from fpdf import FPDF



st.set_page_config(page_title="Contratos do fiscal Marcos Brumatti", layout="wide", menu_items={'About':"Its very cool"})

def inicia_relatorio():
    
              
        
            pdf = FPDF("P", "mm", "A4") 
            pdf.add_page() 
            pdf.set_font("Arial" , size=10) 
    #pdf.cell(200, 10, txt = "Bem-vindo ao Python!", ln = 1, align="C")
    #      pdf.cell(100, 50, txt="Novo texto....avante" )
    #pdf.cell()"C:/Users/Compras/Documents/GitHub/patrimonio/
            pdf.image("img.png", x=60, y=10, w=90, h=20) 
            pdf.text(50, 40, txt="RELATORIO MENSAL DE ACOMPANHAMENTO DE CONTRATO")
    #pdf.rect(x=10, y=70, w=180, h=8)
    #pdf.rect(x=10, y=70, w=60, h=8)
    #
    # pdf.rect(x=70, y=70, w=60, h=8)
            pdf.text(11, 50, txt="CONTRATO N° : "+nro)
            pdf.text(130, 50, txt="DATA DE ABERTURA: "+f"{data_inicio}")
            #pdf.text(180, 50, txt=data_inicio)
            pdf.text(11, 60, txt="CONTRATADO(A)")
            pdf.text(51, 60, str(empresa))
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
            pdf.text(11, 115, txt="PRAZO DO CONTRATO : "+"365 dias")
            pdf.text(121, 105, txt="VALOR DO CONTRATO : "+f"{valor}")
            pdf.text(121, 110, txt="LICITACAO : "+licitacao)
            pdf.text(121, 115, txt="RECURSO : "+f"{recurso}")
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
            pdf.text(51, 185, txt=avaliacao) # texto da avaliação
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
            pdf.text(11, 265, txt="FISCAL DE CONTRATO : "+f"{fiscal_nome}")
            pdf.rect(10, 268, 100, 8)
            pdf.text(11, 273, txt=f"PORTARIA N° {portaria_nro},"+f"DATA: {portaria_data}")
            pdf.rect(10, 276, 100, 8)
            pdf.text(11, 281, txt=f"RELATORIO REFERENTE A : {data_relatorio_1}")

            pdf.rect(110, 260, 90, 8)
            pdf.text(130, 265, txt='ASSINATURA')
            pdf.rect(110, 268, 90, 16)


    
            #pdf.output(f"C:/Users/Compras/Desktop/2025/RELATORIOS/CTR {nro.replace("/", "-")} {empresa}.pdf") 
            # "C:/Users/Compras/Desktop/2025/RELATORIOS/
            pdf.output(f'C:/Users/Compras/Desktop/2025/RELATORIOS/CTR {nro.replace("/", "-")}.pdf') 


df_contratos = pd.read_excel("DADOS_CONTRATOS.xlsx")

df_aditivos = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=1)

df_medicao = pd.read_excel("DADOS_CONTRATOS.xlsx", sheet_name=2)

col = st.columns((1,1,1,1))

df_nro_contrato = df_contratos['contrato'].tolist()
nro = st.sidebar.selectbox("Escolha o contrato", df_nro_contrato)

with st.form("Relatorio"):
    j=11   
    resultado = df_contratos.loc[df_contratos['contrato']==nro]
    print(resultado.dtypes)
    print(resultado.iat[0,2])
    print(resultado['empresa'])
    menina=resultado['empresa']
    objeto = resultado.iat[0,3]
    data_inicio = resultado.iat[0,4].strftime("%d/%m/%Y")
    data_fim = resultado.iat[0,5].strftime("%d/%m/%Y")
    prazo = resultado.iat[0,6]
    
    valor = resultado.iat[0,7]
    
    
    licitacao = resultado.iat[0,8]
    recurso = resultado.iat[0,9]
    fiscal_nome = resultado.iat[0,10]
    portaria_nro = resultado.iat[0,11]
    portaria_data = resultado.iat[0,12].strftime("%d/%m/%Y")
    
    
    n=str(nro)
    #result = resultado[j]['empresa']
    
    empresa = resultado.iat[0,2]
    
    #s2=str(empresa)
    #print(result)
    st.sidebar.write(menina)
    st.sidebar.write(empresa)
    
    #n=int(resultado['id'])-1
    #st.write(n)
    #empresa = st.text_input("EMPRESA", value=f"{df_contratos.iloc[n,2]}")
    #objeto = st.text_input("OBJETO", value=f"{df_contratos.iloc[n,3]}")
    #valor = st.text_input("VALOR", value=f"{df_contratos.iloc[n,7]}")
    #data_inicio = st.text_input("DATA INICIAL", value=f"{df_contratos.iloc[n,4].strftime("%d/%m/%Y")}")
    #data_fim = st.text_input("DATA FINAL", value=f"{df_contratos.iloc[n,5].strftime("%d/%m/%Y")}")
    #licitacao = st.text_input("LICITACAO N°/ANO", value=f"{df_contratos.iloc[n,8]}")
    #portaria_nro = st.text_input("Numero da portaria", value=f"{df_contratos.iloc[n,11]}")
    #portaria_data = st.text_input("Data portaria", value=f"{df_contratos.iloc[n,12].strftime("%d/%m/%Y")}")
    #ordem_inicio = st.text_input("Data da ordem de inicio", value= f"{df_contratos.iloc[n,14]}")
    obs = st.text_input("Observação")
    diligencia = st.text_input("Diligencias")
    ocorrecias = st.text_input("Ocorrencias")
    avaliacao = st.text_input("Avaliação")
    data_relatorio = st.date_input("Data do relatorio")
    data_relatorio_1 = data_relatorio.strftime("%d/%m/%Y")
    if st.form_submit_button():
        inicia_relatorio()









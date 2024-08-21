import streamlit as st 
import pandas as pd
from openpyxl import load_workbook

st.set_page_config("Solicitação de materiais e orçamentos", layout="wide")
st.image("logosanear.png")


def criar_memo():
    memo = load_workbook("modelo_memo.xlsx")
    aba_modelo = memo["Plan1"]

    aba_modelo.cell(row=22, column=4).value = item_orc1
    aba_modelo.cell(row=23, column=4).value = item_orc2
    aba_modelo.cell(row=24, column=4).value = item_orc3
    #print(aba_alunos.cell(row=1, column=2).value)
    memo.save(f"{nome_arquivo}.xlsx")

    

def orcamento():
   st.write("Escolha os produtos")
   lista_orc=[]
   qtdes=[]
   df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=20)
   df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   nomes_orc = df['Descricao'].tolist()
   col=st.columns([1,1,1])
  
   # INSERIR OS PRODUTOS DO ESTOQUE PARA AQUISICAO
   global item_orc1, item_orc2, item_orc3
   
   item_orc1=col[0].selectbox("Descrição 1", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde1=col[1].text_input("Qtde produto 1 : ")
   
   item_orc2=col[0].selectbox("Descrição 2 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde2=col[1].text_input("Qtde produto 2 : ")
   
   item_orc3=col[0].selectbox("Descrição 3 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde3=col[1].text_input("Qtde produto 3 : ")

   # CRIAR AS LISTAS 
   lista_orc.append(item_orc1)
   lista_orc.append(item_orc2)
   lista_orc.append(item_orc3)
   qtdes.append(qtde1)
   qtdes.append(qtde2)
   qtdes.append(qtde3)

   # MOSTRAR NA TELA OS ITENS ESCOLHIDOS
   lista_total=list(zip(lista_orc, qtdes))
   df_orc=pd.DataFrame(lista_total, columns=['Descricao', 'Qtde'])
                       
   col[0].dataframe(df_orc, use_container_width=True)
   #df_orc.to_excel("orcamento.xlsx", index=False)
   #col[1].dataframe(qtdes)
   df_orc.to_excel("orcamento.xlsx", sheet_name='Planilha1')

   

   # DISPARAR PARA FORNECEDORES
   #enviar = col[0].button("ENVIAR POR EMAIL PARA FORNECEDORES", on_click=imprimir)
   #enviar = col[0].button("ENVIAR POR EMAIL PARA FORNECEDORES")
   #col[0].link_button("ENVIAR ORCAMENTO", "https://mail.google.com/mail/u/0/#inbox?compose=new")
   #col[0].link_button("ENVIAR ORCAMENTO", "https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSKkHdPzwgWkcrNGPSHrrKdTGvlGShJwtqqrtkpppgzfSbRtqKjbKXrwzFCvbNDLrMzCrWhP")
   #from openpyxl.workbook import Workbook
   #writer = pd.ExcelWriter("/mount/src/patrimonio/amostra.xlsx")
   #df_orc.to_excel(writer, sheet_name='Planilha1')
   #writer._save()

orcamento()
global nome_arquivo
nome_arquivo=st.text_input("Qual o nome do arquivo? ")
criar_orcamento=enviar = st.button("ENVIAR POR EMAIL PARA FORNECEDORES")
if criar_orcamento:
    
    criar_memo()
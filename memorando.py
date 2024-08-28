import streamlit as st 
import pandas as pd
from openpyxl import load_workbook

st.set_page_config("Solicitação de materiais e orçamentos", layout="wide")
st.image("logosanear.png")
def repete():
    x = st.text_input("Quantos itens deve ter o orçamento ?")
    for i in range(int(x)):
        st.write("Produtos")
        st.write(i)

def criar_memo():
    memo = load_workbook("modelo_memo.xlsx")
    aba_modelo = memo["Plan1"]

    aba_modelo.cell(row=22, column=4).value = item_orc1
    aba_modelo.cell(row=23, column=4).value = item_orc2
    aba_modelo.cell(row=24, column=4).value = item_orc3
    aba_modelo.cell(row=25, column=4).value = item_orc4
    aba_modelo.cell(row=26, column=4).value = item_orc5
    aba_modelo.cell(row=27, column=4).value = item_orc6
    
    aba_modelo.cell(row=22, column=7).value = qtde1
    aba_modelo.cell(row=23, column=7).value = qtde2
    aba_modelo.cell(row=24, column=7).value = qtde3
    aba_modelo.cell(row=25, column=7).value = qtde4
    aba_modelo.cell(row=26, column=7).value = qtde5
    aba_modelo.cell(row=27, column=7).value = qtde6
    
    
    
    
    #print(aba_alunos.cell(row=1, column=2).value)
    memo.save(f"{nome_arquivo}.xlsx")

    

def orcamento():
   st.write("Escolha os produtos")
   lista_orc=[]
   qtdes=[]
   df=pd.read_excel("RPosicao_Estoque_Data_Atual_Excel.xlsx", sheet_name=20)
   df.columns=['Item', 'Descricao', 'Unidade', 'Qtde', 'ValorUnit', 'ValorTotal']
   nomes_orc = df['Item'].tolist()
   
   
   col=st.columns([1,1,1])
  
   # INSERIR OS PRODUTOS DO ESTOQUE PARA AQUISICAO
   global item_orc1, item_orc2, item_orc3, item_orc4, item_orc5, item_orc6
   global qtde1, qtde2, qtde3, qtde4, qtde5, qtde6
   
   item_orc1=col[0].selectbox("Numero do produto", nomes_orc, index=None, placeholder="Digite o nro....")
   resultado_item = df[df['Item']==item_orc1]
   teste=resultado_item[2]
   
   
   col[1].write(teste)
   qtde1=col[2].text_input("Qtde produto 1 : ")
   
   
   
   item_orc2=col[0].selectbox("Descrição 2 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde2=col[1].text_input("Qtde produto 2 : ")
   
   item_orc3=col[0].selectbox("Descrição 3 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde3=col[1].text_input("Qtde produto 3 : ")

   item_orc4=col[0].selectbox("Descrição 4 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde4=col[1].text_input("Qtde produto 4 : ")
   
   item_orc5=col[0].selectbox("Descrição 5 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde5=col[1].text_input("Qtde produto 5 : ")
   
   item_orc6=col[0].selectbox("Descrição 6 :", nomes_orc, index=None, placeholder="Digite o nome....")
   qtde6=col[1].text_input("Qtde produto 6 : ")
   
   # CRIAR AS LISTAS 
   lista_orc.append(resultado_item['Descricao'])
   lista_orc.append(item_orc2)
   lista_orc.append(item_orc3)
   lista_orc.append(item_orc4)
   lista_orc.append(item_orc5)
   lista_orc.append(item_orc6)
   qtdes.append(qtde1)
   qtdes.append(qtde2)
   qtdes.append(qtde3)
   qtdes.append(qtde4)
   qtdes.append(qtde5)
   qtdes.append(qtde6)

   # MOSTRAR NA TELA OS ITENS ESCOLHIDOS
   lista_total=list(zip(lista_orc, qtdes))
   df_orc=pd.DataFrame(lista_total, columns=['Descricao', 'Qtde'])
                       
   col[0].dataframe(df_orc, use_container_width=True)
   #df_orc.to_excel("orcamento.xlsx", index=False)
   #col[1].dataframe(qtdes)
   # df_orc.to_excel("orcamento.xlsx", sheet_name='Planilha1') ##criar tabela em excel com os dados do dataframe criado

   

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
criar_orcamento=enviar = st.button("CRIAR MEMORANDO")
if criar_orcamento:
    
    criar_memo()

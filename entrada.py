import os
import streamlit as st
from supabase import create_client, Client
import pandas as pd
from dotenv import load_dotenv

##contrato;medicao;datamedicao;valor;notafiscal;datanota;datapagto;observacao;protocolo;id


st.set_page_config("Medicoes", layout="wide")

load_dotenv()

url = os.getenv("URL")
key = os.getenv("KEY")
#url: str = os.environ.get("https://hdhvkseneldllvnlvpgc.supabase.co")
#key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkaHZrc2VuZWxkbGx2bmx2cGdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTM3MDM4NTEsImV4cCI6MjAwOTI3OTg1MX0.2Mv5sip2DTHrYY-Ar4WbPNISb1Z3Gtbc9ErhnlohPOM")
#supabase: Client = create_client("https://hdhvkseneldllvnlvpgc.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkaHZrc2VuZWxkbGx2bmx2cGdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTM3MDM4NTEsImV4cCI6MjAwOTI3OTg1MX0.2Mv5sip2DTHrYY-Ar4WbPNISb1Z3Gtbc9ErhnlohPOM")

supabase: Client = create_client(url, key)

## esta função tem o objetivo de listar os contratos que já estão no banco de dados
def lista_contratos():
    resposta = supabase.table("bdmedicaonova").select("contrato").execute()

    olhar = resposta.model_dump()

    lista = [ ]
    i=0
    for i in range(202):
        a = olhar['data'][i]['contrato']
        lista.append(a)
    return list(set(lista))

def alterar():
    a=0
    try:
      nro = st.selectbox("Escolha o contrato", lista_contratos(), key=2)
      altera = supabase.table("bdmedicaonova").select("*").eq("contrato", nro).execute()
      evento = st.dataframe(altera.data, on_select="rerun", selection_mode="single-row")
      a = evento.selection['rows'][0]
      st.write(a)
    except IndexError:
      st.warning("ESCOLHA UMA MEDIÇÃO")

    col1 = st.columns((1,1,1))

    id_altera = altera.data[a]['id']
    st.write(id_altera)
    contrato = col1[0].text_input("Contrato", placeholder=altera.data[a]['contrato'])
    medicao_nro = col1[0].text_input("Número da Medição", placeholder=altera.data[a]['medicao'])
    datamedicao = col1[0].text_input("Data da medicao", placeholder=altera.data[a]['datamedicao'])
    valor = col1[0].text_input("Valor", placeholder=altera.data[a]['valor'])
    nf = col1[1].text_input("Numero da nota fiscal", placeholder=altera.data[a]['notafiscal'])
    datanf = col1[1].text_input("Data de Emissao NF", placeholder=altera.data[a]['datanota'])
    datapgto = col1[1].text_input("Data do pagamento", placeholder=altera.data[a]['datapagto'])
    observ = col1[2].text_input("Observacao", placeholder=altera.data[a]['observacao'])
    prot = col1[2].text_input("Protocolo", placeholder=altera.data[a]['protocolo'])

    if st.button("confirma a alteração?"):
        data_alterar = {
                            "notafiscal":nf, 
                            "datanota":datanf,
                            "datapagto":datapgto,
                            "observacao":observ,
                            "protocolo":prot
                        }
        st.write(data_alterar)
        return supabase.table("bdmedicaonova").update(data_alterar).eq("id", id_altera).execute()


def inserir():
    #ler o total de registros para inserir o id correto
    total = supabase.table("bdmedicaonova").select("*").execute()
    total1=len(total.data)
    st.write(total1)
    #-----------------------------------------------------------------------
    #response = supabase.table("bdmedicao").insert({"contrato": nro_contrato , "medicao_nro": nro_medicao, "medicao_data": data_medicao, "valor": valor}).execute()
    nro = st.selectbox("Escolha o contrato", lista_contratos(), key=1)
    response1 = supabase.table("bdmedicaonova").select("contrato", "medicao", "datamedicao").eq("contrato", nro).execute()
    st.dataframe(response1.data)
    #id_novo = st.text_input("Numero do id")
    col = st.columns((1,1,1))
    ctr = col[0].text_input("Contrato", placeholder=nro)
    med = col[0].text_input("Numero do medicao")
    datamed = col[0].text_input("Data da medição")
    vmed = col[0].text_input("Valor da medicão")
    nf = col[1].text_input("Numero da nota fiscal")
    datanf = col[1].text_input("Data da nota fiscal")
    datapgto = col[1].text_input("Data do pagamento")
    obs = col[2].text_input("Observação")
    prot = col[2].text_input("Numero do protocolo")
    dados = {
                "id": total1+1,
                "contrato" : ctr,
                "medicao" : med,
                "datamedicao" : datamed,
                "valor" : vmed,
                "notafiscal" : nf,
                "datanota" : datanf,
                "datapagto" : datapgto,
                "observacao" : obs,
                "protocolo" : prot
           }
    st.dataframe(dados)
    if st.button("CONFIRMA"):
       return supabase.table("bdmedicaonova").insert(dados).execute()
    #contrato;medicao;datamedicao;valor;notafiscal;datanota;datapagto;observacao;protocolo;id


def main():
    opcoes = ["INSERIR", "ALTERAR"]
    choice = st.sidebar.selectbox("OPCOES", opcoes)

    if choice=="INSERIR":
        inserir()
    
    if choice == "ALTERAR":
        alterar()
    
    #st.button("ALTERAR TESTE", on_click=alterar())
    #st.button("ENTRADA", on_click=inserir())


 
    



main()
   
   #datanota
   #datapagto
   #observacao
   #protocolo
   

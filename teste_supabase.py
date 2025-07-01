import requests


def caninos():
    
    
    #api_key=
    link_api='https://ibhcxtnwnonsnycfgjay.supabase.co'
    
    user='ibhcxtnwnonsnycfgjay'
    
    
    resposta = requests.get(link_api, auth=(user))

    #print(resposta)
    #print(resposta.content)
    dados_requisicao = resposta.json()
    
    
    print(resposta)
    

#caninos()

with open("eng.csv", "r") as f:
    #f.read()
    print(f)
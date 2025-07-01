import requests


def caninos():
    
    
    #api_key=
    link_api='https://ibhcxtnwnonsnycfgjay.supabase.co'
    
    user='ibhcxtnwnonsnycfgjay'
    key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTUxNTM5NjIsImV4cCI6MjAxMDcyOTk2Mn0.PYLOei6RiMbucEqUmTtnmkcjDfIptsiTcNrUCmrBH7c'

    resposta = requests.get(link_api, auth=(user, key))

    #print(resposta)
    #print(resposta.content)
    dados_requisicao = resposta.json()
    
    
    print(resposta)
    

#caninos()

with open("eng.csv", "r") as f:
    #f.read()
    print(f)
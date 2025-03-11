import pandas as pd
import openpyxl

origem = pd.read_excel("orcamento.xlsx", sheet_name=0)

print(origem)

with pd.ExcelWriter('teste_outro.xlsx', mode='a') as writer:  
    origem.to_excel(writer, sheet_name='Sheet_name_3')
    


import openpyxl


def atualizar(nome, idade, sexo):
    workbook = openpyxl.load_workbook("nova.xlsx")
    aba = workbook.active
    aba.append([nome, idade, sexo])
    workbook.save("nova.xlsx")
    
nome = input("Nome :")
idade = input("Idade :")
sexo = input("Sexo:")

atualizar(nome, idade, sexo)
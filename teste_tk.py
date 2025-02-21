import tkinter as tk

global nro1

def inserir():
    nro_processo = tk.Label(janela, text="Numero do processo")
    entrada = tk.Entry(janela)

    nro_processo.grid(row=200, column=100)
    entrada.grid(row=200, column=120)

    cliente = tk.Label(janela, text="Nome do cliente")
    nome_cliente = tk.Entry(janela)

    cliente.grid(row=210, column=100)
    nome_cliente.grid(row=210, column=120)
    uc = tk.Label(janela, text="Unidade consumidora do cliente")
    uc_cliente = tk.Entry(janela)
    uc.grid(row=220, column=100)
    uc_cliente.grid(row=220, column=120)
    
    
    nro1 = entrada.get()
    le1 =tk.Label(frame, text=nro1)
    le1.pack()
    

def mostrar():
    le1 =tk.Label(frame, text="Mostrar dados")
    le1.pack()

def botoes():
    botao_inserir_dados = tk.Button(text="Inserir Dados", command=inserir)
    botao_inserir_dados.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    botao_apres_dados = tk.Button(text="Apresentar dados", command=mostrar)
    botao_apres_dados.grid(row=5, column=10, padx=10, pady=10, sticky='nswe', columnspan=4)
    
    
    
janela = tk.Tk()

janela.title("Cadastro de audiencias")
janela.geometry("1000x1000+100+100")

menubar = tk.Menu()
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Cadastro de processo", font= ('Arial', 12,'bold'), command=inserir)
filemenu.add_command(label="Editar processo", command=mostrar)
filemenu.add_command(label="Mostrar processo", command=mostrar)
filemenu.add_command(label="Mostrar botoes", command=botoes)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=janela.quit)
menubar.add_cascade(label="File", menu=filemenu)
janela.config(menu=menubar)






frame = tk.LabelFrame(janela, text="Dados do cliente")
frame.place(height=100, width=400, rely=0.1, relx=0)









janela.mainloop()


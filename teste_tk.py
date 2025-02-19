import tkinter as tk


janela = tk.Tk()

janela.title("Cadastro de audiencias")
janela.geometry("1000x1000+100+100")
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

frame = tk.LabelFrame(janela, text="Dados do cliente")
frame.place(height=100, width=400, rely=0.1, relx=0)

janela.mainloop()


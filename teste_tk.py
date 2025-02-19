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


janela.mainloop()


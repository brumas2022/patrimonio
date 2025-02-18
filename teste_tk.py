import tkinter as tk


janela = tk.Tk()

janela.title("Cadastro de audiencias")
janela.geometry("1000x1000+100+100")
rotulo = tk.Label(janela, text="Numero do processo")
entrada = tk.Entry(janela)
rotulo.pack()
entrada.pack()



janela.mainloop()


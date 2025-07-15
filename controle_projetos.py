import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Configurações do e-mail
SMTP_SERVER = 'smtp.seu_email.com'
SMTP_PORT = 587
EMAIL_USER = 'seu_email@exemplo.com'
EMAIL_PASSWORD = 'sua_senha'

def enviar_email(gestor_email, assunto, mensagem):
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = EMAIL_USER
    msg['To'] = gestor_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

def analisar_projeto():
    empreendedor = entry_empreendedor.get()
    protocolo = entry_protocolo.get()
    data_entrada = entry_data.get()
    prazo_analise = int(entry_prazo.get())
    analista = entry_analista.get()
    status = entry_status.get()
    gestor_email = entry_gestor.get()

    data_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
    prazo_final = data_entrada + timedelta(days=prazo_analise)

    if prazo_final - datetime.now() <= timedelta(days=10):
        assunto = f'Prazo de Análise do Projeto {protocolo}'
        mensagem = (f'O prazo de análise do projeto {protocolo}, '
                    f'iniciado por {empreendedor}, está se aproximando. '
                    f'Prazo final: {prazo_final.strftime("%Y-%m-%d")}.')
        enviar_email(gestor_email, assunto, mensagem)
        messagebox.showinfo("Sucesso", "E-mail enviado ao gestor.")
    else:
        messagebox.showinfo("Informação", "O prazo não está próximo.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Controle de Análise de Projetos")

# Labels e Entradas
tk.Label(root, text="Empreendedor").grid(row=0, column=0)
entry_empreendedor = tk.Entry(root)
entry_empreendedor.grid(row=0, column=1)

tk.Label(root, text="Protocolo").grid(row=2, column=0)
entry_protocolo = tk.Entry(root)
entry_protocolo.grid(row=2, column=1)

tk.Label(root, text="Data da Entrada (YYYY-MM-DD)").grid(row=4, column=0)
entry_data = tk.Entry(root)
entry_data.grid(row=4, column=1)

tk.Label(root, text="Prazo de Análise (dias)").grid(row=6, column=0)
entry_prazo = tk.Entry(root)
entry_prazo.grid(row=6, column=1)

tk.Label(root, text="Analista").grid(row=8, column=0)
entry_analista = tk.Entry(root)
entry_analista.grid(row=8, column=1)

tk.Label(root, text="Status").grid(row=10, column=0)
entry_status = tk.Entry(root)
entry_status.grid(row=10, column=1)

tk.Label(root, text="E-mail do Gestor").grid(row=12, column=0)
entry_gestor = tk.Entry(root)
entry_gestor.grid(row=12, column=1)

# Botão para analisar projeto
btn_analisar = tk.Button(root, text="Analisar Projeto", command=analisar_projeto)
btn_analisar.grid(row=14, columnspan=2)

root.mainloop()
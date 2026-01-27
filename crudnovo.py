import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Contratos e Medições")
        self.root.geometry("900x600")

        self.setup_db()
        self.create_widgets()
        self.atualizar_tabela()

    def setup_db(self):
        """Cria o banco de dados e a tabela se não existirem."""
        self.conn = sqlite3.connect("gestao_financeira.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contrato TEXT,
                medicao TEXT,
                valor REAL,
                data_medicao TEXT,
                nota_fiscal TEXT,
                data_nf TEXT,
                data_pagamento TEXT
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # Frame de Entrada de Dados
        frame_form = tk.LabelFrame(self.root, text="Dados da Medição", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=10)

        labels = ["Contrato:", "Medição:", "Valor (R$):", "Data Medição (DD/MM/AAAA):", 
                  "Nota Fiscal:", "Data NF:", "Data Pagamento:"]
        self.entries = {}

        for i, text in enumerate(labels):
            row, col = divmod(i, 2)
            tk.Label(frame_form, text=text).grid(row=row, column=col*2, sticky="e", padx=5, pady=2)
            entry = tk.Entry(frame_form)
            entry.grid(row=row, column=col*2+1, padx=5, pady=2)
            self.entries[text] = entry

        # Botões
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Salvar Registro", command=self.salvar, bg="#2ecc71", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Excluir", command=self.deletar, bg="#e74c3c", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(frame_btn, text="Limpar", command=self.limpar_campos, width=15).pack(side="left", padx=5)

        # Tabela (Treeview)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Contrato", "Medição", "Valor", "Data Med.", "NF", "Data NF", "Pagamento"), show="headings")
        
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

    def salvar(self):
        dados = [self.entries[label].get() for label in self.entries]
        
        if not dados[0] or not dados[2]: # Validação simples de Contrato e Valor
            messagebox.showwarning("Aviso", "Contrato e Valor são obrigatórios!")
            return

        try:
            self.cursor.execute("""
                INSERT INTO medicoes (contrato, medicao, valor, data_medicao, nota_fiscal, data_nf, data_pagamento)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, tuple(dados))
            self.conn.commit()
            self.limpar_campos()
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.cursor.execute("SELECT * FROM medicoes")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def deletar(self):
        item_sel = self.tree.selection()
        if not item_sel:
            messagebox.showwarning("Aviso", "Selecione um item para excluir.")
            return
        
        id_reg = self.tree.item(item_sel)['values'][0]
        if messagebox.askyesno("Confirmar", "Deseja excluir este registro?"):
            self.cursor.execute("DELETE FROM medicoes WHERE id=?", (id_reg,))
            self.conn.commit()
            self.atualizar_tabela()

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
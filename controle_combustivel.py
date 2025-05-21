import os
import csv
import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ControleCombustivel:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Abastecimento - Onix")
        self.root.geometry("800x600")
        
        # Definir o arquivo de dados
        self.arquivo_dados = "abastecimentos_onix.csv"
        
        # Criar arquivo de dados se não existir
        if not os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, "w", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["Data", "Quilometragem", "Litros", "Valor Total", "Valor por Litro", "Posto"])
        
        # Criar abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criar as páginas
        self.pagina_registro = ttk.Frame(self.notebook)
        self.pagina_historico = ttk.Frame(self.notebook)
        self.pagina_estatisticas = ttk.Frame(self.notebook)
        
        # Adicionar páginas ao notebook
        self.notebook.add(self.pagina_registro, text="Novo Abastecimento")
        self.notebook.add(self.pagina_historico, text="Histórico")
        self.notebook.add(self.pagina_estatisticas, text="Estatísticas")
        
        # Configurar cada página
        self.configurar_pagina_registro()
        self.configurar_pagina_historico()
        self.configurar_pagina_estatisticas()
    
    def configurar_pagina_registro(self):
        frame = ttk.LabelFrame(self.pagina_registro, text="Registrar Abastecimento")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Data
        ttk.Label(frame, text="Data:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.data_entry = ttk.Entry(frame, width=15)
        self.data_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.data_entry.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))
        
        # Quilometragem
        ttk.Label(frame, text="Quilometragem:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.km_entry = ttk.Entry(frame, width=15)
        self.km_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # Litros
        ttk.Label(frame, text="Litros:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.litros_entry = ttk.Entry(frame, width=15)
        self.litros_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        
        # Valor Total
        ttk.Label(frame, text="Valor Total (R$):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.valor_entry = ttk.Entry(frame, width=15)
        self.valor_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        
        # Posto
        ttk.Label(frame, text="Posto:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.posto_entry = ttk.Entry(frame, width=30)
        self.posto_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        
        # Botão Salvar
        ttk.Button(frame, text="Salvar", command=self.salvar_abastecimento).grid(row=5, column=0, columnspan=2, pady=15)
    
    def configurar_pagina_historico(self):
        frame = ttk.Frame(self.pagina_historico)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criar uma tabela para exibir os dados
        colunas = ("Data", "Quilometragem", "Litros", "Valor Total", "Valor por Litro", "Posto")
        self.tabela = ttk.Treeview(frame, columns=colunas, show="headings")
        
        # Configurar cabeçalhos
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=100)
        
        # Adicionar barra de rolagem
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tabela.yview)
        self.tabela.configure(yscroll=scrollbar.set)
        
        # Posicionar tabela e scrollbar
        self.tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botão para atualizar a tabela
        ttk.Button(self.pagina_historico, text="Atualizar", command=self.carregar_historico).pack(pady=10)
        
        # Carregar dados iniciais
        self.carregar_historico()
    
    def configurar_pagina_estatisticas(self):
        frame = ttk.Frame(self.pagina_estatisticas)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame para estatísticas numéricas
        stats_frame = ttk.LabelFrame(frame, text="Estatísticas Gerais")
        stats_frame.pack(fill=tk.X, pady=10)
        
        # Labels para as estatísticas
        self.total_gasto_label = ttk.Label(stats_frame, text="Total Gasto: R$ 0.00")
        self.total_gasto_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
        
        self.media_consumo_label = ttk.Label(stats_frame, text="Consumo Médio: 0.0 km/l")
        self.media_consumo_label.grid(row=0, column=1, padx=20, pady=5, sticky="w")
        
        self.preco_medio_label = ttk.Label(stats_frame, text="Preço Médio: R$ 0.00/l")
        self.preco_medio_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        
        self.km_total_label = ttk.Label(stats_frame, text="Quilometragem Total: 0 km")
        self.km_total_label.grid(row=1, column=1, padx=20, pady=5, sticky="w")
        
        # Frame para gráficos
        graf_frame = ttk.LabelFrame(frame, text="Gráficos")
        graf_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Criar uma figura para o gráfico
        self.figura = plt.Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figura, graf_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Botão para atualizar estatísticas
        ttk.Button(self.pagina_estatisticas, text="Atualizar Estatísticas", 
                  command=self.atualizar_estatisticas).pack(pady=10)
        
        # Carregar estatísticas iniciais
        self.atualizar_estatisticas()
    
    def salvar_abastecimento(self):
        # Obter dados dos campos
        try:
            data = self.data_entry.get()
            km = float(self.km_entry.get())
            litros = float(self.litros_entry.get())
            valor = float(self.valor_entry.get())
            posto = self.posto_entry.get()
            
            # Calcular valor por litro
            valor_por_litro = round(valor / litros, 2)
            
            # Adicionar dados ao arquivo CSV
            with open(self.arquivo_dados, "a", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([data, km, litros, valor, valor_por_litro, posto])
            
            # Limpar campos
            self.km_entry.delete(0, tk.END)
            self.litros_entry.delete(0, tk.END)
            self.valor_entry.delete(0, tk.END)
            self.posto_entry.delete(0, tk.END)
            
            # Atualizar data para hoje
            self.data_entry.delete(0, tk.END)
            self.data_entry.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))
            
            # Mostrar confirmação
            messagebox.showinfo("Sucesso", "Abastecimento registrado com sucesso!")
            
            # Atualizar histórico e estatísticas
            self.carregar_historico()
            self.atualizar_estatisticas()
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    
    def carregar_historico(self):
        # Limpar tabela
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        
        # Carregar dados do arquivo
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, "r") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pular cabeçalho
                for linha in leitor:
                    if len(linha) >= 6:  # Verificar se a linha tem elementos suficientes
                        self.tabela.insert("", tk.END, values=linha)
    
    def atualizar_estatisticas(self):
        dados = []
        
        # Carregar dados do arquivo
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, "r") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pular cabeçalho
                for linha in leitor:
                    if len(linha) >= 5:  # Verificar se a linha tem elementos suficientes
                        try:
                            dados.append({
                                "data": linha[0],
                                "km": float(linha[1]),
                                "litros": float(linha[2]),
                                "valor": float(linha[3]),
                                "valor_por_litro": float(linha[4]),
                                "posto": linha[5] if len(linha) > 5 else ""
                            })
                        except ValueError:
                            continue
        
        # Calcular estatísticas se houver dados
        if dados:
            # Ordenar dados por quilometragem
            dados_ordenados = sorted(dados, key=lambda x: x["km"])
            
            # Calcular total gasto
            total_gasto = sum(d["valor"] for d in dados)
            self.total_gasto_label.config(text=f"Total Gasto: R$ {total_gasto:.2f}")
            
            # Calcular preço médio por litro
            preco_medio = sum(d["valor"] for d in dados) / sum(d["litros"] for d in dados)
            self.preco_medio_label.config(text=f"Preço Médio: R$ {preco_medio:.2f}/l")
            
            # Calcular quilometragem total (maior - menor)
            if len(dados_ordenados) > 1:
                km_total = dados_ordenados[-1]["km"] - dados_ordenados[0]["km"]
                self.km_total_label.config(text=f"Quilometragem Total: {km_total:.1f} km")
            
            # Calcular consumo médio
            consumos = []
            for i in range(1, len(dados_ordenados)):
                km_diff = dados_ordenados[i]["km"] - dados_ordenados[i-1]["km"]
                litros = dados_ordenados[i-1]["litros"]
                if km_diff > 0 and litros > 0:
                    consumos.append(km_diff / litros)
            
            if consumos:
                consumo_medio = sum(consumos) / len(consumos)
                self.media_consumo_label.config(text=f"Consumo Médio: {consumo_medio:.1f} km/l")
            
            # Gerar gráficos
            self.gerar_graficos(dados_ordenados)
    
    def gerar_graficos(self, dados):
        # Limpar figura anterior
        self.figura.clear()
        
        # Extrair dados para o gráfico
        datas = [d["data"] for d in dados]
        valores_por_litro = [d["valor_por_litro"] for d in dados]
        
        # Criar subplots
        ax1 = self.figura.add_subplot(121)
        ax2 = self.figura.add_subplot(122)
        
        # Gráfico de evolução do preço
        ax1.plot(range(len(datas)), valores_por_litro, 'ro-')
        ax1.set_title('Evolução do Preço do Combustível')
        ax1.set_ylabel('Preço (R$/L)')
        ax1.set_xticks(range(len(datas)))
        ax1.set_xticklabels(datas, rotation=45)
        
        # Gráfico de consumo (se houver pelo menos 2 abastecimentos)
        if len(dados) > 1:
            consumos = []
            kms = []
            for i in range(1, len(dados)):
                km_diff = dados[i]["km"] - dados[i-1]["km"]
                litros = dados[i-1]["litros"]
                if km_diff > 0 and litros > 0:
                    consumos.append(km_diff / litros)
                    kms.append(dados[i]["km"])
            
            if consumos:
                ax2.plot(range(len(consumos)), consumos, 'bo-')
                ax2.set_title('Consumo (km/L)')
                ax2.set_ylabel('Consumo (km/L)')
                ax2.set_xticks(range(len(consumos)))
                ax2.set_xticklabels([f"{km:.0f}" for km in kms], rotation=45)
        
        self.figura.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = ControleCombustivel(root)
    root.mainloop()

"""
Sistema de Fiscalização de Contratos Administrativos
TCE-MT - Relatório Mensal de Fiscalização
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os
import sys
from datetime import datetime
import json

try:
    import customtkinter as ctk
    CTK_AVAILABLE = True
except ImportError:
    CTK_AVAILABLE = False

try:
    import openpyxl
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, HRFlowable, PageBreak)
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# ──────────────────────────────────────────────────────────────────────────────
# BANCO DE DADOS
# ──────────────────────────────────────────────────────────────────────────────

DB_PATH = os.path.join(os.path.dirname(__file__), "fiscalizacao.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS ocorrencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_contrato TEXT NOT NULL,
            mes_ano TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descricao TEXT,
            data_registro TEXT,
            UNIQUE(num_contrato, mes_ano, tipo)
        )
    """)
    conn.commit()
    conn.close()

def salvar_ocorrencia(num_contrato, mes_ano, tipo, descricao):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO ocorrencias (num_contrato, mes_ano, tipo, descricao, data_registro)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(num_contrato, mes_ano, tipo)
        DO UPDATE SET descricao=excluded.descricao, data_registro=excluded.data_registro
    """, (num_contrato, mes_ano, tipo, descricao, datetime.now().strftime("%d/%m/%Y %H:%M")))
    conn.commit()
    conn.close()

def carregar_ocorrencia(num_contrato, mes_ano, tipo):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT descricao FROM ocorrencias WHERE num_contrato=? AND mes_ano=? AND tipo=?",
              (num_contrato, mes_ano, tipo))
    row = c.fetchone()
    conn.close()
    return row[0] if row else ""

def listar_meses_contrato(num_contrato):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT DISTINCT mes_ano FROM ocorrencias WHERE num_contrato=? ORDER BY mes_ano",
              (num_contrato,))
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows]

# ──────────────────────────────────────────────────────────────────────────────
# LEITURA DA PLANILHA EXCEL
# ──────────────────────────────────────────────────────────────────────────────

CAMPOS = ["num_contrato", "objeto", "contratada", "prazo_inicial",
          "prazo_final", "valor", "fiscal", "portaria", "data_portaria"]
CABECALHOS = ["Nº Contrato", "Objeto", "Contratada", "Prazo Inicial",
              "Prazo Final", "Valor (R$)", "Fiscal", "Portaria de Nomeação", "Data da Portaria"]

def ler_planilha(caminho):
    if not OPENPYXL_AVAILABLE:
        raise ImportError("openpyxl não instalado. Execute: pip install openpyxl")
    wb = openpyxl.load_workbook(caminho, data_only=True)
    ws = wb.active
    contratos = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if not any(row):
            continue
        c = {}
        for i, campo in enumerate(CAMPOS):
            val = row[i] if i < len(row) else ""
            if val is None:
                val = ""
            if isinstance(val, datetime):
                val = val.strftime("%d/%m/%Y")
            c[campo] = str(val).strip()
        if c["num_contrato"]:
            contratos.append(c)
    return contratos

# ──────────────────────────────────────────────────────────────────────────────
# GERAÇÃO DO PDF
# ──────────────────────────────────────────────────────────────────────────────

VERDE_ESCURO = colors.HexColor("#1a4c2e")
VERDE_MEDIO = colors.HexColor("#2d7a4f")
VERDE_CLARO = colors.HexColor("#e8f5ee")
CINZA_CLARO = colors.HexColor("#f5f5f5")
AZUL_TCE = colors.HexColor("#003366")

def gerar_pdf(contrato, mes_ano, caminho_saida):
    if not REPORTLAB_AVAILABLE:
        raise ImportError("reportlab não instalado. Execute: pip install reportlab")

    doc = SimpleDocTemplate(
        caminho_saida,
        pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="Relatório de Acompanhamento Mensal do Contrato"
    )

    styles = getSampleStyleSheet()
    s_titulo = ParagraphStyle("titulo",
        fontSize=14, fontName="Helvetica-Bold",
        alignment=TA_CENTER, textColor=AZUL_TCE if False else VERDE_ESCURO,
        spaceAfter=4)
    s_subtitulo = ParagraphStyle("subtitulo",
        fontSize=11, fontName="Helvetica-Bold",
        alignment=TA_CENTER, textColor=VERDE_ESCURO, spaceAfter=8)
    s_secao = ParagraphStyle("secao",
        fontSize=10, fontName="Helvetica-Bold",
        textColor=colors.white, spaceAfter=0)
    s_normal = ParagraphStyle("normal",
        fontSize=9, fontName="Helvetica",
        leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
    s_label = ParagraphStyle("label",
        fontSize=8, fontName="Helvetica-Bold", textColor=colors.HexColor("#555555"))
    s_valor = ParagraphStyle("valor",
        fontSize=9, fontName="Helvetica", leading=13)
    s_rodape = ParagraphStyle("rodape",
        fontSize=7, fontName="Helvetica", textColor=colors.grey, alignment=TA_CENTER)

    story = []

    # ── Cabeçalho ──
    story.append(Paragraph("ESTADO DE MATO GROSSO", ParagraphStyle("uf",
        fontSize=9, fontName="Helvetica", alignment=TA_CENTER,
        textColor=colors.HexColor("#666666"))))
    story.append(Paragraph("RELATÓRIO DE ACOMPANHAMENTO MENSAL DO CONTRATO", s_titulo))
    story.append(Paragraph(f"Referência: {mes_ano}", s_subtitulo))
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE_ESCURO, spaceAfter=10))

    # ── Dados do Contrato ──
    def cabecalho_secao(texto):
        t = Table([[Paragraph(texto, s_secao)]], colWidths=["100%"])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), VERDE_ESCURO),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING", (0,0), (-1,-1), 8),
        ]))
        return t

    story.append(cabecalho_secao("1. IDENTIFICAÇÃO DO CONTRATO"))
    story.append(Spacer(1, 6))

    def linha_dado(label, valor, largura_label="35%", largura_valor="65%"):
        return Table([
            [Paragraph(label, s_label), Paragraph(str(valor), s_valor)]
        ], colWidths=[largura_label, largura_valor],
           style=TableStyle([
               ("BACKGROUND", (0,0), (0,0), CINZA_CLARO),
               ("BACKGROUND", (1,0), (1,0), colors.white),
               ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
               ("INNERGRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
               ("TOPPADDING", (0,0), (-1,-1), 4),
               ("BOTTOMPADDING", (0,0), (-1,-1), 4),
               ("LEFTPADDING", (0,0), (-1,-1), 6),
           ]))

    story.append(linha_dado("Número do Contrato:", contrato["num_contrato"]))
    story.append(Spacer(1, 2))
    story.append(linha_dado("Objeto:", contrato["objeto"]))
    story.append(Spacer(1, 2))
    story.append(linha_dado("Contratada:", contrato["contratada"]))
    story.append(Spacer(1, 2))

    # Prazo e valor lado a lado
    row_prazo = Table([
        [Paragraph("Prazo Inicial:", s_label), Paragraph(contrato["prazo_inicial"], s_valor),
         Paragraph("Prazo Final:", s_label), Paragraph(contrato["prazo_final"], s_valor)]
    ], colWidths=["20%", "30%", "20%", "30%"],
       style=TableStyle([
           ("BACKGROUND", (0,0), (0,0), CINZA_CLARO),
           ("BACKGROUND", (2,0), (2,0), CINZA_CLARO),
           ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
           ("INNERGRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
           ("TOPPADDING", (0,0), (-1,-1), 4),
           ("BOTTOMPADDING", (0,0), (-1,-1), 4),
           ("LEFTPADDING", (0,0), (-1,-1), 6),
       ]))
    story.append(row_prazo)
    story.append(Spacer(1, 2))
    story.append(linha_dado("Valor do Contrato (R$):", contrato["valor"]))
    story.append(Spacer(1, 10))

    # ── Dados do Fiscal ──
    story.append(cabecalho_secao("2. DADOS DO FISCAL"))
    story.append(Spacer(1, 6))
    story.append(linha_dado("Nome do Fiscal:", contrato["fiscal"]))
    story.append(Spacer(1, 2))
    story.append(linha_dado("Portaria de Nomeação:", contrato["portaria"]))
    story.append(Spacer(1, 2))
    story.append(linha_dado("Data da Portaria:", contrato["data_portaria"]))
    story.append(Spacer(1, 10))

    # ── Ocorrências / Diligências / Avaliações / Observações ──
    tipos = [
        ("3. OCORRÊNCIAS DO MÊS", "ocorrencias"),
        ("4. DILIGÊNCIAS REALIZADAS", "diligencias"),
        ("5. AVALIAÇÃO DA EXECUÇÃO", "avaliacoes"),
        ("6. OBSERVAÇÕES GERAIS", "observacoes"),
    ]

    for titulo_sec, tipo in tipos:
        story.append(cabecalho_secao(titulo_sec))
        story.append(Spacer(1, 6))
        texto = carregar_ocorrencia(contrato["num_contrato"], mes_ano, tipo)
        if not texto:
            texto = "Nenhum registro para o período."
        # Caixa de texto com borda
        t = Table([[Paragraph(texto, s_normal)]],
                  colWidths=["100%"],
                  style=TableStyle([
                      ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#aaaaaa")),
                      ("BACKGROUND", (0,0), (-1,-1), colors.white),
                      ("TOPPADDING", (0,0), (-1,-1), 8),
                      ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                      ("LEFTPADDING", (0,0), (-1,-1), 8),
                      ("RIGHTPADDING", (0,0), (-1,-1), 8),
                  ]))
        story.append(t)
        story.append(Spacer(1, 10))

    # ── Assinaturas ──
    story.append(cabecalho_secao("7. ASSINATURAS"))
    story.append(Spacer(1, 20))
    assinatura = Table([
        ["_"*40, "   ", "_"*40],
        [Paragraph(f"<b>{contrato['fiscal']}</b>", ParagraphStyle("ass", fontSize=8, alignment=TA_CENTER)),
         "",
         Paragraph("<b>Autoridade Competente</b>", ParagraphStyle("ass2", fontSize=8, alignment=TA_CENTER))],
        [Paragraph("Fiscal do Contrato", ParagraphStyle("cargo", fontSize=7, textColor=colors.grey, alignment=TA_CENTER)),
         "",
         Paragraph("Cargo / Matrícula", ParagraphStyle("cargo2", fontSize=7, textColor=colors.grey, alignment=TA_CENTER))],
    ], colWidths=["45%", "10%", "45%"],
       style=TableStyle([
           ("ALIGN", (0,0), (-1,-1), "CENTER"),
           ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
           ("TOPPADDING", (0,0), (-1,-1), 3),
       ]))
    story.append(assinatura)
    story.append(Spacer(1, 20))

    # ── Rodapé ──
    story.append(HRFlowable(width="100%", thickness=1, color=VERDE_ESCURO, spaceBefore=10))
    story.append(Paragraph(
        f"Gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M')} | "
        f"Sistema de Fiscalização de Contratos - TCE-MT",
        s_rodape))

    doc.build(story)

# ──────────────────────────────────────────────────────────────────────────────
# INTERFACE GRÁFICA
# ──────────────────────────────────────────────────────────────────────────────

MESES = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
         "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

TIPOS_REGISTRO = [
    ("ocorrencias",  "Ocorrências do Mês"),
    ("diligencias",  "Diligências Realizadas"),
    ("avaliacoes",   "Avaliação da Execução"),
    ("observacoes",  "Observações Gerais"),
]

# Cores e fontes do tema
COR_FUNDO       = "#f0f4f0"
COR_PAINEL      = "#ffffff"
COR_VERDE       = "#1a6b3a"
COR_VERDE_HOVER = "#145c30"
COR_VERDE_CLARO = "#e8f5ee"
COR_BORDA       = "#c8ddd0"
COR_TEXTO       = "#1a1a1a"
COR_TEXTO_SEC   = "#3a6b4a"
FONTE_TITULO    = ("Segoe UI", 11, "bold")
FONTE_LABEL     = ("Segoe UI", 9)
FONTE_NORMAL    = ("Segoe UI", 9)
FONTE_BOTAO     = ("Segoe UI", 9, "bold")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        init_db()
        self.title("Fiscalização de Contratos – TCE-MT")
        self.geometry("1200x750")
        self.minsize(950, 650)
        self.configure(bg=COR_FUNDO)

        self.contratos = []
        self.contrato_selecionado = None

        self._build_ui()
        self._criar_planilha_modelo()

    # ── Layout principal ──────────────────────────────────────────────────────

    def _build_ui(self):
        # Barra de título
        topo = tk.Frame(self, bg=COR_VERDE, height=56)
        topo.pack(fill="x")
        topo.pack_propagate(False)
        tk.Label(topo, text="⚖  Fiscalização de Contratos Administrativos – TCE-MT",
                 bg=COR_VERDE, fg="white",
                 font=("Segoe UI", 13, "bold")).pack(side="left", padx=16, pady=10)

        # Container principal
        corpo = tk.Frame(self, bg=COR_FUNDO)
        corpo.pack(fill="both", expand=True, padx=12, pady=10)

        # ── Coluna esquerda: lista de contratos ──
        col_esq = tk.Frame(corpo, bg=COR_PAINEL, relief="flat",
                            highlightthickness=1, highlightbackground=COR_BORDA)
        col_esq.pack(side="left", fill="y", padx=(0,10))
        col_esq.pack_propagate(False)
        col_esq.configure(width=270)

        tk.Label(col_esq, text="Contratos", bg=COR_PAINEL,
                 fg=COR_TEXTO_SEC, font=FONTE_TITULO).pack(anchor="w", padx=12, pady=(10,4))

        # Botões de importar e modelo
        btn_frame = tk.Frame(col_esq, bg=COR_PAINEL)
        btn_frame.pack(fill="x", padx=10, pady=(0,6))
        self._btn(btn_frame, "📂 Importar Planilha", self._importar, "#2d7a4f").pack(fill="x", pady=2)
        self._btn(btn_frame, "📋 Baixar Modelo Excel", self._abrir_modelo, "#5a8f6a").pack(fill="x", pady=2)

        # Lista de contratos
        lista_frame = tk.Frame(col_esq, bg=COR_PAINEL)
        lista_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        sb = ttk.Scrollbar(lista_frame)
        sb.pack(side="right", fill="y")
        self.lista = tk.Listbox(lista_frame, yscrollcommand=sb.set,
                                 bg="white", fg=COR_TEXTO,
                                 font=FONTE_NORMAL, relief="flat",
                                 selectbackground=COR_VERDE, selectforeground="white",
                                 activestyle="none", borderwidth=0,
                                 highlightthickness=1, highlightbackground=COR_BORDA)
        self.lista.pack(side="left", fill="both", expand=True)
        sb.config(command=self.lista.yview)
        self.lista.bind("<<ListboxSelect>>", self._selecionar_contrato)

        # ── Coluna direita: detalhe + registros ──
        col_dir = tk.Frame(corpo, bg=COR_FUNDO)
        col_dir.pack(side="left", fill="both", expand=True)

        # Painel de dados do contrato
        self.painel_dados = tk.LabelFrame(col_dir, text=" Dados do Contrato ",
                                           bg=COR_PAINEL, fg=COR_TEXTO_SEC,
                                           font=FONTE_TITULO, relief="flat",
                                           highlightthickness=1,
                                           highlightbackground=COR_BORDA)
        self.painel_dados.pack(fill="x", pady=(0,8))
        self.labels_dados = {}
        self._build_painel_dados()

        # Seleção de mês/ano
        mes_frame = tk.Frame(col_dir, bg=COR_PAINEL,
                              highlightthickness=1, highlightbackground=COR_BORDA)
        mes_frame.pack(fill="x", pady=(0,8))

        tk.Label(mes_frame, text="Mês de Referência:", bg=COR_PAINEL,
                 font=FONTE_LABEL, fg=COR_TEXTO).pack(side="left", padx=10, pady=8)

        self.var_mes = tk.StringVar(value=MESES[datetime.now().month - 1])
        cb_mes = ttk.Combobox(mes_frame, textvariable=self.var_mes,
                               values=MESES, width=12, state="readonly")
        cb_mes.pack(side="left", padx=4)

        self.var_ano = tk.StringVar(value=str(datetime.now().year))
        anos = [str(a) for a in range(2020, datetime.now().year + 3)]
        cb_ano = ttk.Combobox(mes_frame, textvariable=self.var_ano,
                               values=anos, width=7, state="readonly")
        cb_ano.pack(side="left", padx=4)

        self._btn(mes_frame, "🔍 Carregar Registros", self._carregar_registros,
                  COR_VERDE).pack(side="left", padx=10)

        # Notebook de registros
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background=COR_FUNDO)
        style.configure("TNotebook.Tab", font=FONTE_LABEL,
                         padding=[10, 5], background=COR_VERDE_CLARO)
        style.map("TNotebook.Tab", background=[("selected", COR_VERDE)],
                  foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(col_dir)
        self.notebook.pack(fill="both", expand=True)

        self.areas_texto = {}
        for tipo, titulo in TIPOS_REGISTRO:
            frame = tk.Frame(self.notebook, bg=COR_PAINEL)
            self.notebook.add(frame, text=f"  {titulo}  ")

            tk.Label(frame, text=titulo, bg=COR_PAINEL, fg=COR_TEXTO_SEC,
                     font=FONTE_TITULO).pack(anchor="w", padx=12, pady=(10,4))
            tk.Label(frame, text="Descreva detalhadamente abaixo:", bg=COR_PAINEL,
                     font=FONTE_LABEL, fg="#666666").pack(anchor="w", padx=12)

            txt_frame = tk.Frame(frame, bg=COR_PAINEL)
            txt_frame.pack(fill="both", expand=True, padx=12, pady=(4,8))
            sb2 = tk.Scrollbar(txt_frame)
            sb2.pack(side="right", fill="y")
            txt = tk.Text(txt_frame, yscrollcommand=sb2.set,
                          font=("Segoe UI", 10), relief="flat",
                          bg="#fafafa", fg=COR_TEXTO,
                          wrap="word", padx=8, pady=8,
                          highlightthickness=1, highlightbackground=COR_BORDA)
            txt.pack(fill="both", expand=True)
            sb2.config(command=txt.yview)
            self.areas_texto[tipo] = txt

        # Barra de ações
        barra_acoes = tk.Frame(col_dir, bg=COR_PAINEL,
                                highlightthickness=1, highlightbackground=COR_BORDA)
        barra_acoes.pack(fill="x", pady=(8,0))

        self._btn(barra_acoes, "💾  Salvar Registros", self._salvar_registros,
                  COR_VERDE, 12).pack(side="left", padx=10, pady=8)
        self._btn(barra_acoes, "📄  Gerar PDF do Relatório", self._gerar_pdf,
                  "#b55a00", 12).pack(side="left", padx=4, pady=8)

        self.status_var = tk.StringVar(value="Importe uma planilha Excel para começar.")
        tk.Label(barra_acoes, textvariable=self.status_var,
                 bg=COR_PAINEL, font=FONTE_LABEL, fg="#555555").pack(side="right", padx=12)

    def _btn(self, parent, texto, comando, cor, pad=8):
        b = tk.Button(parent, text=texto, command=comando,
                      bg=cor, fg="white", font=FONTE_BOTAO,
                      relief="flat", bd=0, cursor="hand2",
                      padx=pad, pady=5,
                      activebackground=COR_VERDE_HOVER, activeforeground="white")
        b.bind("<Enter>", lambda e: b.config(bg=self._escurecer(cor)))
        b.bind("<Leave>", lambda e: b.config(bg=cor))
        return b

    @staticmethod
    def _escurecer(hex_cor):
        r = int(hex_cor[1:3], 16)
        g = int(hex_cor[3:5], 16)
        b = int(hex_cor[5:7], 16)
        r = max(0, r - 20); g = max(0, g - 20); b2 = max(0, b - 20)
        return f"#{r:02x}{g:02x}{b2:02x}"

    def _build_painel_dados(self):
        campos_display = [
            ("num_contrato", "Nº Contrato", 0, 0),
            ("objeto",       "Objeto",      0, 2),
            ("contratada",   "Contratada",  1, 0),
            ("valor",        "Valor (R$)",  1, 2),
            ("prazo_inicial","Prazo Inicial",2, 0),
            ("prazo_final",  "Prazo Final", 2, 2),
            ("fiscal",       "Fiscal",      3, 0),
            ("portaria",     "Portaria",    3, 2),
            ("data_portaria","Data Portaria",4, 0),
        ]
        for campo, label, row, col in campos_display:
            tk.Label(self.painel_dados, text=label+":", bg=COR_PAINEL,
                     font=("Segoe UI", 8, "bold"), fg="#555555").grid(
                row=row, column=col, sticky="w", padx=(14,2), pady=3)
            var = tk.StringVar(value="—")
            tk.Label(self.painel_dados, textvariable=var, bg=COR_VERDE_CLARO,
                     font=FONTE_NORMAL, fg=COR_TEXTO,
                     relief="flat", padx=6, pady=2,
                     width=24, anchor="w").grid(
                row=row, column=col+1, sticky="ew", padx=(0,12), pady=3)
            self.labels_dados[campo] = var
        for i in [1, 3, 5, 7]:
            self.painel_dados.grid_columnconfigure(i, weight=1)

    # ── Ações ─────────────────────────────────────────────────────────────────

    def _importar(self):
        if not OPENPYXL_AVAILABLE:
            messagebox.showerror("Erro", "Instale o openpyxl:\npip install openpyxl")
            return
        caminho = filedialog.askopenfilename(
            title="Selecionar Planilha de Contratos",
            filetypes=[("Excel", "*.xlsx *.xls"), ("Todos", "*.*")])
        if not caminho:
            return
        try:
            self.contratos = ler_planilha(caminho)
            self.lista.delete(0, "end")
            for c in self.contratos:
                self.lista.insert("end", f"  {c['num_contrato']}")
            self.status_var.set(f"✔ {len(self.contratos)} contrato(s) importado(s).")
        except Exception as e:
            messagebox.showerror("Erro ao importar", str(e))

    def _selecionar_contrato(self, event=None):
        sel = self.lista.curselection()
        if not sel:
            return
        self.contrato_selecionado = self.contratos[sel[0]]
        for campo, var in self.labels_dados.items():
            var.set(self.contrato_selecionado.get(campo, "—") or "—")
        self._carregar_registros()

    def _carregar_registros(self):
        if not self.contrato_selecionado:
            return
        num = self.contrato_selecionado["num_contrato"]
        mes_ano = self._mes_ano_atual()
        for tipo, _ in TIPOS_REGISTRO:
            txt = self.areas_texto[tipo]
            txt.delete("1.0", "end")
            conteudo = carregar_ocorrencia(num, mes_ano, tipo)
            if conteudo:
                txt.insert("1.0", conteudo)
        self.status_var.set(f"Registros de {mes_ano} carregados para contrato {num}.")

    def _salvar_registros(self):
        if not self.contrato_selecionado:
            messagebox.showwarning("Atenção", "Selecione um contrato primeiro.")
            return
        num = self.contrato_selecionado["num_contrato"]
        mes_ano = self._mes_ano_atual()
        for tipo, _ in TIPOS_REGISTRO:
            texto = self.areas_texto[tipo].get("1.0", "end").strip()
            salvar_ocorrencia(num, mes_ano, tipo, texto)
        self.status_var.set(f"✔ Registros de {mes_ano} salvos com sucesso!")
        messagebox.showinfo("Salvo", f"Registros de {mes_ano} salvos com sucesso!")

    def _gerar_pdf(self):
        if not self.contrato_selecionado:
            messagebox.showwarning("Atenção", "Selecione um contrato primeiro.")
            return
        if not REPORTLAB_AVAILABLE:
            messagebox.showerror("Erro", "Instale o reportlab:\npip install reportlab")
            return
        # Salva antes de gerar
        self._salvar_registros()
        mes_ano = self._mes_ano_atual()
        num = self.contrato_selecionado["num_contrato"].replace("/", "-")
        nome_sugerido = f"Relatorio_{num}_{mes_ano.replace('/', '_')}.pdf"
        caminho = filedialog.asksaveasfilename(
            title="Salvar Relatório PDF",
            defaultextension=".pdf",
            initialfile=nome_sugerido,
            filetypes=[("PDF", "*.pdf")])
        if not caminho:
            return
        try:
            gerar_pdf(self.contrato_selecionado, mes_ano, caminho)
            self.status_var.set(f"✔ PDF gerado: {os.path.basename(caminho)}")
            messagebox.showinfo("PDF Gerado", f"Relatório salvo em:\n{caminho}")
            # Tenta abrir automaticamente
            if sys.platform == "win32":
                os.startfile(caminho)
            elif sys.platform == "darwin":
                os.system(f'open "{caminho}"')
            else:
                os.system(f'xdg-open "{caminho}"')
        except Exception as e:
            messagebox.showerror("Erro ao gerar PDF", str(e))

    def _mes_ano_atual(self):
        mes = MESES.index(self.var_mes.get()) + 1
        return f"{mes:02d}/{self.var_ano.get()}"

    def _criar_planilha_modelo(self):
        """Cria modelo Excel automaticamente se não existir."""
        if not OPENPYXL_AVAILABLE:
            return
        caminho = os.path.join(os.path.dirname(__file__), "modelo_contratos.xlsx")
        if os.path.exists(caminho):
            return
        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Contratos"
            from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
            fill_cab = PatternFill("solid", fgColor="1a6b3a")
            font_cab = Font(bold=True, color="FFFFFF", name="Segoe UI", size=10)
            borda = Border(
                left=Side(style="thin", color="AAAAAA"),
                right=Side(style="thin", color="AAAAAA"),
                top=Side(style="thin", color="AAAAAA"),
                bottom=Side(style="thin", color="AAAAAA")
            )
            for col, cab in enumerate(CABECALHOS, 1):
                cell = ws.cell(row=1, column=col, value=cab)
                cell.font = font_cab
                cell.fill = fill_cab
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.border = borda
            ws.row_dimensions[1].height = 22
            larguras = [18, 35, 30, 14, 14, 16, 25, 22, 16]
            for col, larg in enumerate(larguras, 1):
                ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = larg
            # Linha de exemplo
            exemplo = ["2024/001", "Prestação de serviços de limpeza e conservação",
                       "Empresa Exemplo Ltda.", "01/01/2024", "31/12/2024",
                       "120.000,00", "João da Silva", "Portaria nº 001/2024", "02/01/2024"]
            fill_ex = PatternFill("solid", fgColor="e8f5ee")
            for col, val in enumerate(exemplo, 1):
                cell = ws.cell(row=2, column=col, value=val)
                cell.fill = fill_ex
                cell.border = borda
                cell.font = Font(name="Segoe UI", size=9)
            wb.save(caminho)
        except Exception:
            pass

    def _abrir_modelo(self):
        caminho = os.path.join(os.path.dirname(__file__), "modelo_contratos.xlsx")
        if not os.path.exists(caminho):
            self._criar_planilha_modelo()
        if os.path.exists(caminho):
            if sys.platform == "win32":
                os.startfile(caminho)
            elif sys.platform == "darwin":
                os.system(f'open "{caminho}"')
            else:
                os.system(f'xdg-open "{caminho}"')
            self.status_var.set(f"Modelo aberto: {caminho}")
        else:
            messagebox.showinfo("Modelo", f"Modelo disponível em:\n{caminho}")


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = App()
    app.mainloop()

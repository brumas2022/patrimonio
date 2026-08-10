import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Gestão de Licenciamento Ambiental",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------------------------------------------------------
# INICIALIZAÇÃO DE DADOS (SESSION STATE)
# -----------------------------------------------------------------------------
if "empresas" not in st.session_state:
    st.session_state.empresas = [
        {"id": 1, "nome": "Empresa Alfa S.A.", "cnpj": "12.345.678/0001-90", "contato": "contato@alfa.com"},
        {"id": 2, "nome": "Beta Mineração Ltda", "cnpj": "98.765.432/0001-10", "contato": "beta@mineracao.com"}
    ]

if "tipos_licencas" not in st.session_state:
    st.session_state.tipos_licencas = [
        {"sigla": "LP", "nome": "Licença Prévia", "prazo_padrao_dias": 365, "documentos": "EIA/RIMA, Certidão de Uso do Solo, Anotação de Responsabilidade Técnica (ART)"},
        {"sigla": "LI", "nome": "Licença de Instalação", "prazo_padrao_dias": 730, "documentos": "PCA, Plano de Gerenciamento de Resíduos, Outorga de Água"},
        {"sigla": "LO", "nome": "Licença de Operação", "prazo_padrao_dias": 1460, "documentos": "Relatório de Cumprimento de Condicionantes, Alvará do Corpo de Bombeiros"}
    ]

if "projetos" not in st.session_state:
    st.session_state.projetos = [
        {
            "id": 101,
            "empresa_id": 1,
            "nome_projeto": "Expansão da Planta Industrial",
            "tipo_licenca": "LI",
            "valor": 45000.00,
            "data_emissao": datetime.now().date() - timedelta(days=100),
            "data_vencimento": datetime.now().date() + timedelta(days=20), # Vencendo em breve
            "status": "Em andamento"
        },
        {
            "id": 102,
            "empresa_id": 2,
            "nome_projeto": "Nova Jazida Sul",
            "tipo_licenca": "LP",
            "valor": 78000.00,
            "data_emissao": datetime.now().date() - timedelta(days=300),
            "data_vencimento": datetime.now().date() + timedelta(days=65),
            "status": "Em andamento"
        }
    ]

# -----------------------------------------------------------------------------
# BARRA LATERAL (LOGO E NAVEGAÇÃO)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🌱 Licenciamento Pro")
    
    # Espaço para inserção do Logotipo
    logo_file = "lh_logo.jpeg" **st.file_uploader("Upload do Logotipo", type=["png", "jpg", "jpeg"])
    if logo_file:
        st.image(logo_file, use_container_width=True)
    else:
        st.info("💡 Você pode carregar a logo da sua empresa acima.")

    st.markdown("---")
    
    # Menu Principal
    menu_principal = st.radio(
        "Navegação Menu Principal:",
        [
            "🏢 Cadastros de Empresas",
            "📜 Regras de Licenças & Docs",
            "🚀 Projetos de Licenciamento",
            "📊 Relatórios Gerenciais",
            "⏰ Controle de Vencimentos e Alertas"
        ]
    )

# -----------------------------------------------------------------------------
# 1. CADASTRO DE EMPRESAS (CLIENTES)
# -----------------------------------------------------------------------------
if menu_principal == "🏢 Cadastros de Empresas":
    st.title("🏢 Gestão de Empresas (Clientes)")
    
    sub_menu = st.radio("Selecione uma ação:", ["Inserir Empresa", "Editar Empresa", "Remover Empresa"], horizontal=True)

    if sub_menu == "Inserir Empresa":
        st.subheader("Cadastrar Nova Empresa")
        with st.form("form_add_empresa"):
            nome = st.text_input("Nome / Razão Social")
            cnpj = st.text_input("CNPJ")
            contato = st.text_input("E-mail de Contato")
            submitted = st.form_submit_button("Salvar Empresa")
            
            if submitted:
                if nome:
                    novo_id = max([e["id"] for e in st.session_state.empresas], default=0) + 1
                    st.session_state.empresas.append({"id": novo_id, "nome": nome, "cnpj": cnpj, "contato": contato})
                    st.success(f"Empresa '{nome}' cadastrada com sucesso!")
                else:
                    st.error("O campo Nome/Razão Social é obrigatório.")

    elif sub_menu == "Editar Empresa":
        st.subheader("Editar Dados da Empresa")
        if not st.session_state.empresas:
            st.info("Nenhuma empresa cadastrada.")
        else:
            empresa_sel_nome = st.selectbox("Selecione a empresa:", [e["nome"] for e in st.session_state.empresas])
            empresa_dict = next(e for e in st.session_state.empresas if e["nome"] == empresa_sel_nome)
            
            with st.form("form_edit_empresa"):
                novo_nome = st.text_input("Nome / Razão Social", value=empresa_dict["nome"])
                novo_cnpj = st.text_input("CNPJ", value=empresa_dict["cnpj"])
                novo_contato = st.text_input("E-mail de Contato", value=empresa_dict["contato"])
                submitted = st.form_submit_button("Atualizar Empresa")
                
                if submitted:
                    empresa_dict["nome"] = novo_nome
                    empresa_dict["cnpj"] = novo_cnpj
                    empresa_dict["contato"] = novo_contato
                    st.success("Dados atualizados com sucesso!")
                    st.rerun()

    elif sub_menu == "Remover Empresa":
        st.subheader("Remover Empresa")
        if not st.session_state.empresas:
            st.info("Nenhuma empresa cadastrada.")
        else:
            empresa_sel_nome = st.selectbox("Selecione a empresa para remover:", [e["nome"] for e in st.session_state.empresas])
            empresa_dict = next(e for e in st.session_state.empresas if e["nome"] == empresa_sel_nome)
            
            st.warning(f"Atenção: Ao remover '{empresa_dict['nome']}', certifique-se de que não haja pendências associadas.")
            if st.button("Confirmar Exclusão"):
                st.session_state.empresas = [e for e in st.session_state.empresas if e["id"] != empresa_dict["id"]]
                # Remove projetos associados
                st.session_state.projetos = [p for p in st.session_state.projetos if p["empresa_id"] != empresa_dict["id"]]
                st.success("Empresa e seus dados vinculados foram removidos!")
                st.rerun()

    # Exibição da tabela de empresas
    st.markdown("---")
    st.subheader("Empresas Cadastradas")
    if st.session_state.empresas:
        df_emp = pd.DataFrame(st.session_state.empresas)
        st.dataframe(df_emp, use_container_width=True)

# -----------------------------------------------------------------------------
# 2. CADASTRO DE TIPOS DE LICENÇA E DOCUMENTOS NECESSÁRIOS
# -----------------------------------------------------------------------------
elif menu_principal == "📜 Regras de Licenças & Docs":
    st.title("📜 Tipos de Licença, Prazos e Documentos")
    st.write("Defina de forma independente as exigências e os prazos de validade para cada modalidade ambiental.")

    with st.expander("➕ Adicionar Novo Tipo de Licença", expanded=False):
        with st.form("form_add_licenca"):
            sigla = st.text_input("Sigla (ex: LP, LI, LO, LAS)").upper()
            nome_lic = st.text_input("Nome Completo (ex: Licença de Operação)")
            prazo_dias = st.number_input("Prazo Padrão de Validade (dias)", min_value=30, value=365)
            docs = st.text_area("Documentos Necessários / Checklist (separados por vírgula)")
            
            submitted = st.form_submit_button("Salvar Tipo de Licença")
            if submitted:
                if sigla and nome_lic:
                    st.session_state.tipos_licencas.append({
                        "sigla": sigla, "nome": nome_lic, "prazo_padrao_dias": prazo_dias, "documentos": docs
                    })
                    st.success(f"Tipo de licença '{sigla}' cadastrado com sucesso!")
                    st.rerun()

    # Tabela de Tipos Cadastrados
    st.subheader("Tipos Configurados")
    if st.session_state.tipos_licencas:
        df_lic = pd.DataFrame(st.session_state.tipos_licencas)
        st.dataframe(df_lic, use_container_width=True)

# -----------------------------------------------------------------------------
# 3. CADASTRO DE PROJETOS DE LICENCIAMENTO
# -----------------------------------------------------------------------------
elif menu_principal == "🚀 Projetos de Licenciamento":
    st.title("🚀 Cadastro de Projetos de Licenciamento")

    if not st.session_state.empresas:
        st.warning("Cadastre ao menos uma Empresa antes de criar projetos.")
    else:
        empresa_map = {e["nome"]: e["id"] for e in st.session_state.empresas}
        empresa_nome_sel = st.selectbox("Selecione a Empresa (Cliente):", list(empresa_map.keys()))
        empresa_id_sel = empresa_map[empresa_nome_sel]

        st.markdown("---")
        st.subheader(f"Cadastrar Projeto para: {empresa_nome_sel}")

        tipos_siglas = [t["sigla"] for t in st.session_state.tipos_licencas] if st.session_state.tipos_licencas else ["Outro"]

        with st.form("form_novo_projeto"):
            col1, col2 = st.columns(2)
            with col1:
                nome_proj = st.text_input("Nome do Projeto / Atividade")
                tipo_lic = st.selectbox("Tipo de Licença", tipos_siglas)
                valor_proj = st.number_input("Valor do Projeto (R$)", min_value=0.0, value=5000.0, step=500.0)
            
            with col2:
                dt_emissao = st.date_input("Data de Emissão da Licença")
                
                # Busca prazo padrão para preencher a data sugerida
                prazo_default = 365
                for t in st.session_state.tipos_licencas:
                    if t["sigla"] == tipo_lic:
                        prazo_default = t["prazo_padrao_dias"]
                        
                dt_vencimento = st.date_input("Data de Vencimento da Licença", value=dt_emissao + timedelta(days=prazo_default))
                status_proj = st.selectbox("Status Atual", ["Em andamento", "Aprovado", "Pendente Doc", "Cancelado"])

            # Exibe documentos requeridos do tipo de licença selecionado
            doc_requeridos = next((t["documentos"] for t in st.session_state.tipos_licencas if t["sigla"] == tipo_lic), "Nenhum documento pré-configurado.")
            st.info(f"📋 **Documentos exigidos para {tipo_lic}:** {doc_requeridos}")

            sub_proj = st.form_submit_button("Cadastrar Projeto")
            
            if sub_proj:
                novo_id_p = max([p["id"] for p in st.session_state.projetos], default=100) + 1
                st.session_state.projetos.append({
                    "id": novo_id_p,
                    "empresa_id": empresa_id_sel,
                    "nome_projeto": nome_proj,
                    "tipo_licenca": tipo_lic,
                    "valor": valor_proj,
                    "data_emissao": dt_emissao,
                    "data_vencimento": dt_vencimento,
                    "status": status_proj
                })
                st.success("Projeto vinculado à empresa com sucesso!")

# -----------------------------------------------------------------------------
# 4. RELATÓRIOS GERENCIAIS
# -----------------------------------------------------------------------------
elif menu_principal == "📊 Relatórios Gerenciais":
    st.title("📊 Relatórios e Indicadores")

    if not st.session_state.projetos:
        st.info("Nenhum projeto cadastrado para exibição de relatórios.")
    else:
        # Preparação da base consolidada
        df_proj = pd.DataFrame(st.session_state.projetos)
        df_emp = pd.DataFrame(st.session_state.empresas)
        df_completo = pd.merge(df_proj, df_emp, left_on="empresa_id", right_on="id", suffixes=("_proj", "_emp"))

        tab1, tab2, tab3 = st.tabs(["Por Empresa", "Por Projeto", "Por Tipo de Licença"])

        with tab1:
            st.subheader("Resumo por Empresa")
            emp_filtro = st.selectbox("Filtrar por Empresa:", ["Todas"] + list(df_emp["nome"].unique()))
            
            df_tab1 = df_completo if emp_filtro == "Todas" else df_completo[df_completo["nome_emp"] == emp_filtro]
            
            st.metric("Total de Projetos", len(df_tab1))
            st.metric("Valor Total Contratado (R$)", f"R$ {df_tab1['valor'].sum():,.2f}")
            st.dataframe(df_tab1[["nome_emp", "nome_projeto", "tipo_licenca", "valor", "data_vencimento", "status"]], use_container_width=True)

        with tab2:
            st.subheader("Projetos Detalhados")
            st.dataframe(df_completo[["id_proj", "nome_projeto", "nome_emp", "tipo_licenca", "valor", "status"]], use_container_width=True)

        with tab3:
            st.subheader("Distribuição por Tipo de Licença")
            group_tipo = df_completo.groupby("tipo_licenca").agg(
                Quantidade=("id_proj", "count"),
                Valor_Total=("valor", "sum")
            ).reset_index()
            st.dataframe(group_tipo, use_container_width=True)

# -----------------------------------------------------------------------------
# 5. CONTROLE DE VENCIMENTOS E ALERTAS POR EMAIL
# -----------------------------------------------------------------------------
elif menu_principal == "⏰ Controle de Vencimentos e Alertas":
    st.title("⏰ Controle de Vencimento de Licenças")
    
    if not st.session_state.projetos:
        st.info("Nenhum projeto/licença cadastrado.")
    else:
        df_p = pd.DataFrame(st.session_state.projetos)
        df_e = pd.DataFrame(st.session_state.empresas)
        df_alertas = pd.merge(df_p, df_e, left_on="empresa_id", right_on="id")

        col1, col2 = st.columns(2)
        with col1:
            dias_antecedencia = st.slider("Disparar alerta para licenças a vencer em até (dias):", 5, 120, 30)
        
        # Filtro de datas
        hoje = datetime.now().date()
        df_alertas["dias_para_vencer"] = df_alertas["data_vencimento"].apply(lambda x: (x - hoje).days)
        
        df_filtrado = df_alertas[df_alertas["dias_para_vencer"] <= dias_antecedencia]

        st.subheader(f"Licenças em atenção ou com vencimento nos próximos {dias_antecedencia} dias")
        
        if df_filtrado.empty:
            st.success(" Nenhuma licença com vencimento próximo dentro desse período!")
        else:
            st.warning(f"Foram encontradas {len(df_filtrado)} licenças prestes a vencer!")
            st.dataframe(
                df_filtrado[["nome_projeto", "nome", "tipo_licenca", "data_vencimento", "dias_para_vencer", "contato"]],
                use_container_width=True
            )

            st.markdown("---")
            st.subheader("📩 Disparo de Notificação por E-mail")

            with st.form("form_envio_email"):
                email_destino = st.text_input("E-mail de Destino (Responsável / Cliente):", value="responsavel.ambiental@empresa.com")
                assunto = st.text_input("Assunto do E-mail", value=f"[ALERTA] Licenças Prestes a Vencer ({len(df_filtrado)} encontradas)")
                
                # Corpo do e-mail montado dinamicamente
                corpo_default = f"Olá,\n\nAs seguintes licenças ambientais estão prestes a vencer:\n\n"
                for _, row in df_filtrado.iterrows():
                    corpo_default += f"- Projeto: {row['nome_projeto']} | Empresa: {row['nome']} | Vencimento: {row['data_vencimento']} ({row['dias_para_vencer']} dias)\n"
                
                corpo_email = st.text_area("Mensagem:", value=corpo_default, height=180)
                
                btn_disparar = st.form_submit_button("🚀 Simular Disparo de Alerta por E-mail")
                
                if btn_disparar:
                    st.success(f"Alerta enviado com sucesso para: **{email_destino}**!")
                    st.toast("Notificação emitida!")

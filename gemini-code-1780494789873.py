import datetime
import pandas as pd


class RelatorioObra:

    def __init__(self):
        # Lista que vai armazenar os dicionários de cada etapa/etapa da obra
        self.dados_obra = []

    def incluir_etapa(self):
        print("\n" + "=" * 30)
        print("  INCLUSÃO DE ETAPA DA OBRA  ")
        print("=" * 30)

        # 1. Validação da Data
        while True:
            data_str = input(
                "Data da medição (DD/MM/AAAA) [Deixe em branco para hoje]: "
            ).strip()
            if not data_str:
                data = datetime.date.today().strftime("%d/%m/%Y")
                break
            try:
                datetime.datetime.strptime(data_str, "%d/%m/%Y")
                data = data_str
                break
            except ValueError:
                print("❌ Formato de data inválido! Use DD/MM/AAAA.")

        # 2. Entrada de Textos
        etapa = input("Nome da Etapa (ex: Fundação, Alvenaria): ").strip()
        descricao = input("Descrição do que foi feito: ").strip()

        # 3. Validação do Percentual
        while True:
            try:
                progresso = float(
                    input("Percentual de conclusão desta etapa (0 a 100): ")
                )
                if 0 <= progresso <= 100:
                    break
                print("❌ O progresso deve ser um número entre 0 e 100.")
            except ValueError:
                print("❌ Digite um valor numérico válido.")

        # 4. Validação do Custo
        while True:
            try:
                custo = float(input("Custo desta etapa (R$): "))
                if custo >= 0:
                    break
                print("❌ O custo não pode ser negativo.")
            except ValueError:
                print("❌ Digite um valor numérico válido (use ponto para centavos).")

        # Salvando os dados no "módulo"
        registro = {
            "Data": data,
            "Etapa": etapa,
            "Descrição": descricao,
            "Progresso (%)": progresso,
            "Custo (R$)": custo,
        }

        self.dados_obra.append(registro)
        print("\n✅ Etapa incluída com sucesso!")

    def visualizar_relatorio(self):
        if not self.dados_obra:
            print("\n⚠️ Nenhum dado lançado ainda.")
            return

        df = pd.DataFrame(self.dados_obra)
        print("\n" + "=" * 50)
        print("          RELATÓRIO ATUAL DA OBRA          ")
        print("=" * 50)
        print(df.to_string(index=False))
        print("=" * 50)
        print(f"Total Investido Até Agora: R$ {df['Custo (R$)'].sum():,.2f}")
        print(f"Média de Progresso das Etapas: {df['Progresso (%)'].mean():.2f}%")

    def exportar_dados(self):
        if not self.dados_obra:
            print("\n⚠️ Não há dados para exportar.")
            return

        df = pd.DataFrame(self.dados_obra)

        # Exporta para Excel e CSV
        df.to_csv("relatorio_obra.csv", index=False, encoding="utf-8-sig")
        df.to_excel("relatorio_obra.xlsx", index=False)
        print("\n💾 Arquivos 'relatorio_obra.csv' e 'relatorio_obra.xlsx' gerados!")


# --- MENU PRINCIPAL (SIMULANDO O SISTEMA DA RECEITA) ---
def menu():
    sistema = RelatorioObra()

    while True:
        print("\n" + "#" * 40)
        print("  SISTEMA DE GERENCIAMENTO DE OBRAS  ")
        print("#" * 40)
        print("1. Incluir Novo Progresso/Etapa")
        print("2. Visualizar Relatório em Tela")
        print("3. Exportar Relatório (Excel/CSV)")
        print("4. Sair")

        opcao = input("\nEscolha uma opção (1-4): ").strip()

        if opcao == "1":
            sistema.incluir_etapa()
        elif opcao == "2":
            sistema.visualizar_relatorio()
        elif opcao == "3":
            sistema.exportar_dados()
        elif opcao == "4":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
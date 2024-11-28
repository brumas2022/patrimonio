import streamlit as st
import pandas as pd



def main():
    st.title("Destacador de Linhas em DataFrame")
    preco = st.number_input("entre numero")
    calcular_imposto = lambda x: x*0.3 if x<500 else x*0.9
    st.write(calcular_imposto(preco))

    # Carregar o DataFrame
    uploaded_file = pd.read_excel("controle_nad.xlsx", sheet_name=0)
    if uploaded_file is not None:
        df = uploaded_file
        st.dataframe(df)

        # Selecionar coluna e valor para a condição
        #column_to_filter = st.selectbox("Selecione a coluna", df.columns)
        #filter_value = st.text_input("Digite o valor para filtrar")

        # Aplicar a condição e destacar a linha
        if df[df.columns['entrega total']=='ok']:
            df_filtered = df.style.apply(
                lambda x: ['background: lightblue'], axis=1
            )
            st.dataframe(df_filtered)

if __name__ == "__main__":
    main()
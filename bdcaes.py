from dotenv import load_dotenv
import streamlit as st 
import os
#import supabase
st.set_page_config("Cadastro dos caes", layout="wide")

load_dotenv()
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")

from supabase import create_client, Client
supabase: Client = create_client('https://ibhcxtnwnonsnycfgjay.supabase.co',
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE1Mzk2MiwiZXhwIjoyMDEwNzI5OTYyfQ.W9t9sqi_odq3kV2WovKCVfMXcFGprFOgai9Us9_rTQA')

st.header("Animais na ARPAA")

total = supabase.table("caninos").select("nome").execute()
tot = len(total.data)
st.sidebar.write("Animais que ja foram ajudados:", tot)

total_adotados = supabase.table("caninos").select("nome").eq("adotado", "True").execute()
tot_adotados = len(total_adotados.data)
st.sidebar.write("Total atual de animais na ARPAA:", tot_adotados)

total_atual = supabase.table("caninos").select("nome").eq("adotado", "False").eq("vivo", "True").execute()
tot_atual = len(total_atual.data)
st.sidebar.write("Total atual de animais na ARPAA:", tot_atual)

genero = st.sidebar.selectbox("Escolha o genero do animal", ("macho", "femea"))
castrado = st.sidebar.selectbox("Defina de castração", ("True", "False"))
resposta = supabase.table("caninos").select("nome", "genero", "entrada", "foto").eq("adotado", "False").eq("vivo", "True").eq("genero", f"{genero}").eq("castrado", f"{castrado}" ).execute()
st.dataframe(resposta.data)
a=len(resposta.data)
st.write(f"Ainda temos {a} {genero}")
#exemplo = supabase.table("caninos").select("foto").execute()
#imagem = supabase.storage.from_("Meninos").get_public_url("Femeas/princesa.jpg")
imagem1 = supabase.storage.from_("Meninos").download("Femeas/princesa.jpg")
foto = supabase.table("caninos").select("*").execute()
st.image(imagem1, width=400)
#st.dataframe(foto.data[43]['foto'])
#st.image(foto.data[78]['foto'], width=300)
#st.image(foto, width=200)
#st.image(imagem, width=400)
#st.write([imagem], width=400)
#st.write(exemplo)
#st.image(exemplo)
#st.dataframe(resposta.data[data="nome"])

#res = supabase.storage.from_('Meninos').get_public_url('Femeas/Betina.jpg')
#sql = "SELECT * FROM caninos"
#df = pd.read_sql_query(sql, con=engine)

#df_filtro = df[df["foto"]!=""]
#df_filtro = df_filtro.set_index('id')
#st.dataframe(df_filtro)
#col1, col2, col3, col4 = st.columns((1,1,1,1))
#col1.image(df_filtro['foto'][43], caption=df_filtro['nome'][43], use_column_width="always")st.image(str(res))


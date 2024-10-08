from dotenv import load_dotenv
import streamlit as st 
import os
st.set_page_config("Cadastro dos caes", layout="wide")

load_dotenv()
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")

from supabase import create_client, Client
supabase: Client = create_client('https://ibhcxtnwnonsnycfgjay.supabase.co',
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE1Mzk2MiwiZXhwIjoyMDEwNzI5OTYyfQ.W9t9sqi_odq3kV2WovKCVfMXcFGprFOgai9Us9_rTQA')

st.header("Animais na ARPAA")
genero = st.selectbox("Escolha o genero do animal", ("macho", "femea"))
castrado = st.selectbox("Defina de castração", ("True", "False"))
resposta = supabase.table("caninos").select("nome", "genero", "entrada").eq("adotado", "False").eq("vivo", "True").eq("genero", f"{genero}").eq("castrado", f"{castrado}" ).execute()
st.dataframe(resposta.data)
a=len(resposta.data)
st.write(f"Ainda temos {a} {genero}")
#st.dataframe(resposta.data[data="nome"])

#res = supabase.storage.from_('Meninos').get_public_url('Femeas/Betina.jpg')
#st.image(str(res))


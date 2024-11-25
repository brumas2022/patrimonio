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
exemplo = 'https://ibhcxtnwnonsnycfgjay.supabase.co/storage/v1/object/sign/Meninos/Femeas/Betina.jpg?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJNZW5pbm9zL0ZlbWVhcy9CZXRpbmEuanBnIiwiaWF0IjoxNzMyNTY3OTQxLCJleHAiOjE3MzMxNzI3NDF9.aIt9tjBxecz2lFiQRv1Uv21dklQtVtNzC_-QmygtCZo&t=2024-11-25T20%3A52%3A21.837Z'
imagem = supabase.storage.from_("Meninos").get_public_url("Femeas/antonieta.jpg")
st.image(imagem)
st.image(exemplo)
#st.dataframe(resposta.data[data="nome"])

#res = supabase.storage.from_('Meninos').get_public_url('Femeas/Betina.jpg')
#st.image(str(res))


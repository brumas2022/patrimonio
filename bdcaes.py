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

def inicio():
    total = supabase.table("caninos").select("nome").execute()
    tot = len(total.data)
    st.write("Animais que ja foram ajudados nos ultimos anos:", tot)

    total_adotados = supabase.table("caninos").select("nome").eq("adotado", "True").execute()
    tot_adotados = len(total_adotados.data)
    st.write("Total de animais que foram adotados:", tot_adotados)

    total_atual = supabase.table("caninos").select("nome").eq("adotado", "False").eq("vivo", "True").execute()
    tot_atual = len(total_atual.data)
    st.write("Total atual de animais na ARPAA:", tot_atual)
    
def castrados():
    st.header("Animais que já foram castrados")
    machos_castrados = supabase.table("caninos").select("nome", "genero", "entrada").eq("adotado", "False").eq("vivo", "True").eq("genero", "macho").eq("castrado", "True").execute()
    femeas_castradas = supabase.table("caninos").select("nome", "genero", "entrada").eq("adotado", "False").eq("vivo", "True").eq("genero", "femea").eq("castrado", "True").execute()
    qtde_machos_castrados = len(machos_castrados.data)
    qtde_femeas_castradas = len(femeas_castradas.data)
    st.markdown(f"São {qtde_machos_castrados} machos castrados")
    st.dataframe(machos_castrados.data)
    st.markdown(f"São {qtde_femeas_castradas} femeas castradas")
    st.dataframe(femeas_castradas.data)
    
def nao_castrados():
    st.header("Animais que ainda não foram castrados")
    machos_nao_castrados = supabase.table("caninos").select("nome", "genero", "entrada").eq("adotado", "False").eq("vivo", "True").eq("genero", "macho").eq("castrado", "False").execute()
    femeas_nao_castradas = supabase.table("caninos").select("nome", "genero", "entrada").eq("adotado", "False").eq("vivo", "True").eq("genero", "femea").eq("castrado", "False").execute()
    qtde_machos_nao_castrados = len(machos_nao_castrados.data)
    qtde_femeas_nao_castradas = len(femeas_nao_castradas.data)
    st.markdown(f"São {qtde_machos_nao_castrados} machos nao castrados")
    st.dataframe(machos_nao_castrados.data)
    st.markdown(f"São {qtde_femeas_nao_castradas} femeas nao castradas")
    st.dataframe(femeas_nao_castradas.data) 
       
def apresenta():
    st.header("Animais que estão abrigados atualmente")
    imagem1 = supabase.storage.from_("Meninos").download("Femeas/princesa.jpg")
    imagen2 = supabase.storage.from_("Meninos").download("Femeas/michele.jpg")
    imagen3 = supabase.storage.from_("Meninos").download("Femeas/gorda.jpg")
    imagen4 = supabase.storage.from_("Meninos").download("Femeas/dina.jpg")
    col = st.columns((1,1,1,1))
    col[0].image(imagem1, width=200, caption="Princesa")
    col[1].image(imagen2, width=200, caption="Michele")
    col[2].image(imagen3, width=200, caption="Gorda")
    col[3].image(imagen4, width=200, caption="Dina")

def apresenta1():
    st.header("Animais que já viraram estrelinha")
    imagem1 = supabase.storage.from_("Meninos").download("Machos/bob.jpg")
    imagen2 = supabase.storage.from_("Meninos").download("Machos/Bebezao.jpg")
    imagen3 = supabase.storage.from_("Meninos").download("Machos/branquelo.jpg")
    imagen4 = supabase.storage.from_("Meninos").download("Machos/nico.jpg")
    col = st.columns((1,1,1,1))
    col[0].image(imagem1, width=200, caption="Bob")
    col[1].image(imagen2, width=200, caption="Bebezao")
    col[2].image(imagen3, width=200, caption="Branquelo")
    col[3].image(imagen4, width=200, caption="Nico")
    


fotos = st.sidebar.button("FOTOS", use_container_width=True)
estrelinhas = st.sidebar.button("ESTRELINHAS", use_container_width=True)
cast = st.sidebar.button("ANIMAIS CASTRADOS", use_container_width=True)
nao_cast = st.sidebar.button("ANIMAIS NAO CASTRADOS", use_container_width=True)

if nao_cast:
    nao_castrados()
    
elif cast:
    
    castrados()
    
elif estrelinhas:
    
    apresenta1()
    
elif fotos:
    
    apresenta()
    
else:
    
    inicio()
   
#exemplo = supabase.table("caninos").select("foto").execute()
#imagem = supabase.storage.from_("Meninos").get_public_url("Femeas/princesa.jpg")

#if insert:
#    up = supabase.storage.from_("Meninos").upload(file="img.png", path="Femeas/img.png")

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


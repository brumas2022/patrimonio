import streamlit as st 
import folium
from streamlit_folium import st_folium
import pandas as pd
import time

def poco_tubular(nome, lat, long, tipo):
    st.header(f"{nome}", divider="orange")
    st.markdown(f"Esta é a localização do {tipo}")
    m = folium.Map(location=[lat, long], zoom_start=16)
    folium.Marker(
    [lat, long], popup=f"{nome}", tooltip=f"{nome}"
    ).add_to(m)
    
    return st_folium(m, width=725, returned_objects=[])
    
df = pd.read_excel("UNIDADES_SANEAR_2025", sheet_name=0)
#df = pd.read_csv("pocos.csv")

local = df["nome"].tolist()

escolha = st.sidebar.radio("Escolha o poço tubular", local)

resultado = df[df['nome']==escolha]

nome = resultado.iat[0,0]
lat = resultado.iat[0,1]
long = resultado.iat[0,2]
tipo = resultado.iat[0,3]
poco_tubular(nome, lat, long, tipo)



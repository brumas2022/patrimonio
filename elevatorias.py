import streamlit as st 
import folium
from streamlit_folium import st_folium
import pandas as pd


def ipanema():
    st.header("EEE IPANEMA", divider="orange")
    st.markdown("Esta é a localização da elevatoria")
    m = folium.Map(location=[-16.478585175815436, -54.64800486531498], zoom_start=16)
    folium.Marker(
    [-16.478585175815436, -54.64800486531498], popup="EEE IPANEMA", tooltip="Vila Goulart"
    ).add_to(m)
    
    return st_folium(m, width=725, returned_objects=[])
def canaa():
    st.header("EEE CANAA", divider="orange")
    st.markdown("Esta é a localização da elevatoria")
    m = folium.Map(location=[-16.475795739518535, -54.64324120001045], zoom_start=16)
    folium.Marker(
    [-16.475795739518535, -54.64324120001045], popup="EEE CANAA", tooltip="Vila Goulart"
    ).add_to(m)
    
    return st_folium(m, width=725, returned_objects=[])
    

    
    
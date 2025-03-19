import streamlit as st 
import folium
from streamlit_folium import st_folium
import pandas as pd
import time

   
def p03():
    st.subheader("P03 - Atlantico", divider="orange")
    #m = folium.Map(location=(-16.468104952605543, -54.57546160244493))
    #st_folium(m)
    #st.button("PAre")
    poi = pd.DataFrame({
    'lat': [-16.468104952605543],
    'lon': [-54.57546160244493],
    'name': ['ATLANTICO']
    })
    st.map(poi)
def p02():
    st.header("P02 - Cohab", divider="orange")
    st.markdown("Esta é a localização do poço")
    pausa = False
    while not pausa:
            m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
            folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
            ).add_to(m)

              # call to render Folium map in Streamlit
            st_data = st_folium(m, width=725)
            pausa = st.button("pausa")
            #time.sleep(100)
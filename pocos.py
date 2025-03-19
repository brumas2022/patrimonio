import streamlit as st 
import folium
from streamlit_folium import st_folium
import pandas as pd
import time

   
def p03():
    st.subheader("P03 - Atlantico", divider="orange")
    m = folium.Map(location=[-16.468104952605543, -54.57546160244493], zoom_start=16)
    folium.Marker(
    [-16.468104952605543, -54.57546160244493], popup="Vila Goulart", tooltip="Vila Goulart"
    ).add_to(m)
    
    return st_folium(m, width=725, returned_objects=[])
    #poi = pd.DataFrame({
    #'lat': [-16.468104952605543],
    #'lon': [-54.57546160244493],
    #'name': ['ATLANTICO']
    #})
    #st.map(poi)
def p04():
    st.header("P04 - Vila Goulart", divider="orange")
    st.markdown("Esta é a localização do poço")
    m = folium.Map(location=[-16.48933413559257, -54.63979329041073], zoom_start=16)
    folium.Marker(
    [-16.48933413559257, -54.63979329041073], popup="Vila Goulart", tooltip="Vila Goulart"
    ).add_to(m)
    
    return st_folium(m, width=725, returned_objects=[])
            

    #call to render Folium map in Streamlit
    #st_data = st_folium(m, width=725)
            
    
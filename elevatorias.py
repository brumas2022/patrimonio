import streamlit as st 
import folium
from streamlit_folium import st_folium
import pandas as pd
def ipanema():
    st.subheader("EEE IPANEMA", divider="orange")
    #m = folium.Map(location=(-16.478585175815436, -54.64800486531498))
    #st_folium(m)
    #st.button("PAre")
    poi = pd.DataFrame({
    'lat': [-16.478585175815436],
    'lon': [-54.64800486531498],
    'name': ['IPANEMA']
    })
    st.map(poi)
    
def p01():
    st.subheader("P01 - Atlantico", divider="orange")
    st.markdown("Esta é a localização do poço")
def p02():
    st.header("P02 - Cohab", divider="orange")
    st.markdown("Esta é a localização do poço")
    
    
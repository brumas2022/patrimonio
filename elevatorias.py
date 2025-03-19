import streamlit as st 
import folium
from streamlit_folium import st_folium
def ipanema():
    st.empty()
    st.subheader("EEE IPANEMA", divider="orange")
    m = folium.Map(location=(-16.478585175815436, -54.64800486531498), zoom_control=True)
    a=st_folium(m)
    
def p01():
    st.subheader("P01 - Atlantico", divider="orange")
    st.markdown("Esta é a localização do poço")
def p02():
    st.header("P02 - Cohab", divider="orange")
    st.markdown("Esta é a localização do poço")
    
    
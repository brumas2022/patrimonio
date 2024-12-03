import streamlit as st 
from streamlit_calendar import calendar

calen = calendar(events={2,3}, options={})
calen.event("Evento1")

st.write(calen)
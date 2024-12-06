import streamlit as st 
from streamlit_calendar import calendar
import shelve

with shelve.open('TesteDB') as db:
    db['entrada']=10
    db['saida']=20
    
print(db["entrada"])

col = st.columns((1,1,1,1,1))
dia = col[0].date_input("Entre com o dia:")
entrada_manha = col[1].time_input("Entrada manha :", value=None)
saida_manha = col[2].time_input("Saida manha :")
entrada_tarde = col[3].time_input("Entrada tarde :")
saida_tarde = col[4].time_input("Saida tarde :")




calendar_events = [
    {
        "title": "Event 1",
        "start": "2024-12-01T08:30:00",
        "end": "2024-12-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""
calen = calendar(events=calendar_events, custom_css=custom_css)
st.dataframe(calen)
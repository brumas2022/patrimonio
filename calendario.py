import streamlit as st 
from streamlit_calendar import calendar


dia = st.date_input("Entre com o dia:")
entrada_manha = st.time_input("Entrada manha :", value="now")
saida_manha = st.time_input("Saida manha :")
entrada_tarde = st.time_input("Entrada tarde :")
saida_tarde = st.time_input("Saida tarde :")




calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
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
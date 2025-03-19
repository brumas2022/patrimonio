import streamlit as st
import os
#from dotenv import load_dotenv
import st_pages 
from st_pages import add_page_title
from elevatorias import ipanema
from pocos import p03, p04


with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#st.header("Estrutura do SANEAR", divider="orange")
    
        


senha = st.sidebar.selectbox(
    "Escolha uma opção",
    ("Poços", "Elevatorias de Esgoto", "Agencias Comerciais", "Reservatorios")
)
if senha == "Poços":
   st.sidebar.button("P - 03", on_click=p03, use_container_width=True)
   st.sidebar.button("P - 04", on_click=p04, use_container_width=True)
   st.sidebar.link_button("P - 03", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 04", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 05", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 06", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 07", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 08", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 09", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 10", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 11", "https://estoque1.streamlit.app", use_container_width=True)
   st.sidebar.link_button("P - 12", "https://estoque1.streamlit.app", use_container_width=True)
   

if senha=="Elevatorias de Esgoto":
    st.sidebar.button("Canaa", on_click=ipanema, use_container_width=True)
    st.sidebar.link_button("Rio Vermelho", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Canivete", "https://estoque1.streamlit.app",  use_container_width=True)
    st.sidebar.link_button("Ipanema", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Nova Era", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
    st.sidebar.link_button("Padre Lothar", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)
    st.sidebar.link_button("Lajeadinho", "https://loja1dosebo.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Jardim das Flores", "https://sebodomarcao-g4cnpbtuc8aclncvnvzr4e.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Centro", "https://www.atribunamt.com.br/opiniao-do-leitor/2024/05/entre-o-passado-e-o-futuro-o-papel-do-museu-rosa-bororo-na-historia-em-rondonopolis/", use_container_width=True)
    st.sidebar.link_button("Sitio Farias", "http://inquilinos.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Bispo Casaldaliga", "http://controle1.streamlit.app", use_container_width=True)

    #st.sidebar.markdown(":red[Trabalhadores de todo mundo, UNI-VOS]")
    #st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Agencias Comerciais":
    
    st.sidebar.link_button("Centro", "https://www.cifraclub.com.br/raul-seixas/aluga-se/", use_container_width=True)
    st.sidebar.link_button("Vila Operaria", "https://www.cifraclub.com.br/henrique-e-juliano/flor-e-o-beija-flor/", use_container_width=True)
    
    st.sidebar.markdown(":sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:  :sunglasses:")

if senha=="Reservatorios":
    st.sidebar.link_button("Aeroporto", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("UFR", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Atlantico", "https://estoque1.streamlit.app",  use_container_width=True)
    st.sidebar.link_button("P. Universitario", "https://estoque1.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Globo Recreio", "https://www.youtube.com/watch?v=JnxCIRxt3kQ&t=19s", use_container_width=True)
    st.sidebar.link_button("Cidade Alta", "https://www.mercadopago.com.br/integrations/v1/web-payment-checkout.js", use_container_width=True)
    st.sidebar.link_button("ETA", "https://loja1dosebo.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Jardim das Flores", "https://sebodomarcao-g4cnpbtuc8aclncvnvzr4e.streamlit.app/", use_container_width=True)
    st.sidebar.link_button("Monte Libano", "https://www.atribunamt.com.br/opiniao-do-leitor/2024/05/entre-o-passado-e-o-futuro-o-papel-do-museu-rosa-bororo-na-historia-em-rondonopolis/", use_container_width=True)
    st.sidebar.link_button("Magnolia", "http://inquilinos.streamlit.app", use_container_width=True)
    st.sidebar.link_button("Buriti", "http://controle1.streamlit.app", use_container_width=True)
        
    





#cols = st.columns((0.75,1,1.25,1,1,1))
#cols[0].link_button("PCI", "https://www.pciconcursos.com.br/", use_container_width=True)
#cols[1].link_button("SANEAR", "https://www.sanearmt.com.br", use_container_width=True)
#cols[2].link_button("PREFEITURA", "http://www.rondonopolis.mt.gov.br", use_container_width=True)
#cols[3].link_button("A TRIBUNA", "https://www.atribunamt.com.br", use_container_width=True)
#cols[4].link_button("CATRACA", "https://catracalivre.com.br/", use_container_width=True)
#cols[5].link_button("DOU", "https://www.in.gov.br/servicos/diario-oficial-da-uniao", use_container_width=True)



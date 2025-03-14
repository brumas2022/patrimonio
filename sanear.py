import streamlit as st
import telebot
import psycopg2
import os
from dotenv import load_dotenv
from st_pages import show_pages_from_config, add_page_title




senha = st.sidebar.selectbox(
    "Escolha uma opção",
    ("Poços", "Elevatorias de Esgoto", "Agencias Comerciais", "Reservatórios")
)
if senha == "Poços":
   st.sidebar.link_button("PT - 01", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 02", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 03", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 04", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 05", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 06", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 07", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 08", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 09", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 10", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 11", "https://estoque1.streamlit.app")
   st.sidebar.link_button("PT - 12", "https://estoque1.streamlit.app")
   

if senha=="Elevatorias":
    st.sidebar.link_button("Canaa", "https://estoque1.streamlit.app", use_container_width=True)
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
    st.sidebar.markdown(":violet[Aquele que serve a uma revolução ara no mar]")
    #st.sidebar.markdown(":musical_note:")
    #st.sidebar.audio("Eu Amo Esse Homem (Trecho).mp3", loop=True)
    #audio_file = open('06-Hc3.mp3','rb') #enter the filename with filepath
    #audio_bytes = audio_file.read() #reading the file
    st.sidebar.write("HC3")
    #st.sidebar.audio(audio_bytes, format='audio/mpeg') #displaying the audio
    st.sidebar.audio('06-Hc3.mp3',format='audio/mpeg')
    surfin = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/20%20-%20Surfin%20Bird.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvMjAgLSBTdXJmaW4gQmlyZC5tcDMiLCJpYXQiOjE3MzE2MTUyODgsImV4cCI6MTczNDIwNzI4OH0.uYKjP4pROOOZmUdHR1SppybMrYbxAKYv5T33xWf8ifE&t=2024-11-14T20%3A15%3A22.667Z'
    cantares = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzE2MTUwMzcsImV4cCI6MTczNDIwNzAzN30.QYl4S-YOaxFR-ADZfOm9i9-sgWMF6ku9c54nHToNhA0&t=2024-11-14T20%3A11%3A11.889Z'
    chico = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Chico%20Buarque%20-%20Vai%20Passar.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9DaGljbyBCdWFycXVlIC0gVmFpIFBhc3Nhci5tcDMiLCJpYXQiOjE3MzI1NjEwNzEsImV4cCI6MTc2NDA5NzA3MX0.w_oB288ldIZaC15_J2na5OlhW2xu_ypUv_ZCA0Zb3BQ&t=2024-11-25T18%3A57%3A51.202Z'
    abreu = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Fernanda%20Abreu%20-%20Katia%20Flavia.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9GZXJuYW5kYSBBYnJldSAtIEthdGlhIEZsYXZpYS5tcDMiLCJpYXQiOjE3MzI1NjExMTcsImV4cCI6MTc2NDA5NzExN30.5FNWk3kCm-KwrmKrPMhE7zVe4BvymEwEzLHlMt6j6Vs&t=2024-11-25T18%3A58%3A38.225Z'
    bohe = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Queen%20-%20Bohemian%20Rhapsody.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9RdWVlbiAtIEJvaGVtaWFuIFJoYXBzb2R5Lm1wMyIsImlhdCI6MTczMjU2MTE1MSwiZXhwIjoxNzY0MDk3MTUxfQ.fmpVTG9ZiXvLu7J9-0ztlYaJCRkYX7YUFJOEroY0sWc&t=2024-11-25T18%3A59%3A12.014Z'
    pedro = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Raul%20Seixas%20-%20Meu%20Amigo%20Pedro.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9SYXVsIFNlaXhhcyAtIE1ldSBBbWlnbyBQZWRyby5tcDMiLCJpYXQiOjE3MzI1NjExNzYsImV4cCI6MTc2NDA5NzE3Nn0.BWtQzY4eZiPUBttNE9xCbgGm8OHck8g9xcZZkJfWqrM&t=2024-11-25T18%3A59%3A36.950Z'
    zegeraldo = 'https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/songs/Ze%20Geraldo%20-%20Meiga%20Senhorita.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzb25ncy9aZSBHZXJhbGRvIC0gTWVpZ2EgU2VuaG9yaXRhLm1wMyIsImlhdCI6MTczMjU2NTk4MywiZXhwIjoxNzY0MTAxOTgzfQ.Ifu6e3bbQA7SPz7403G7JoQ036C1_tHeOSEJvIbTkYg&t=2024-11-25T20%3A19%3A43.675Z' 
    
    #audio1_file = open('https://hdhvkseneldllvnlvpgc.supabase.co/storage/v1/object/sign/PMSB-tabelas/Tabela5-10/01-Cantares.mp3?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJQTVNCLXRhYmVsYXMvVGFiZWxhNS0xMC8wMS1DYW50YXJlcy5tcDMiLCJpYXQiOjE3MzA5MjIxMDYsImV4cCI6MTczMTUyNjkwNn0.E7gXHtius5OTuz6slQvzV3B367HdPwW86WChKAE_Jpw&t=2024-11-06T19%3A42%3A18.206Z', 'rb')
    #audio1_bytes = audio1_file.read()
    st.sidebar.audio(cantares, format='audio/mpeg')
    st.sidebar.audio(surfin, format='audio/mpeg')
    st.sidebar.audio(chico, format='audio/mpeg')
    st.sidebar.audio(abreu, format='audio/mpeg')
    st.sidebar.audio(bohe, format='audio/mpeg')
    st.sidebar.audio(pedro, format='audio/mpeg')
    st.sidebar.audio(zegeraldo, format='audio/mpeg')

st.header(":green[SANEAR]", divider="orange")
st.markdown("Estrutura do SANEAR")
st.write("---")
#st.image("IMG_20220616_220024.jpg")
st.image("img.png")



cols = st.columns((0.75,1,1.25,1,1,1))
cols[0].link_button("PCI", "https://www.pciconcursos.com.br/", use_container_width=True)
cols[1].link_button("SANEAR", "https://www.sanearmt.com.br", use_container_width=True)
cols[2].link_button("PREFEITURA", "http://www.rondonopolis.mt.gov.br", use_container_width=True)
cols[3].link_button("A TRIBUNA", "https://www.atribunamt.com.br", use_container_width=True)
cols[4].link_button("CATRACA", "https://catracalivre.com.br/", use_container_width=True)
cols[5].link_button("DOU", "https://www.in.gov.br/servicos/diario-oficial-da-uniao", use_container_width=True)


a = st.selectbox("Escolha a opção desejada",("Elogio SANEAR", "Reclamação SANEAR", "Sugestão SANEAR"))
if a == "Elogio SANEAR":
  nome = st.text_input("Digite seu nome")
  prompt = st.chat_input("Say something")
  if prompt:
      st.write(f"{nome} enviou a seguinte mensagem : {prompt}")
elif a == "Reclamação SANEAR":
  st.markdown("Reclamação SANEAR")
  st.balloons()
  
elif a ==  "Sugestão SANEAR":
  st.markdown("Sugestão SANEAR")
  st.snow()
  st.write("---")
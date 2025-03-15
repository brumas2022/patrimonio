import yaml
import streamlit as st 
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
    )

authenticator.login(location='sidebar')
    
if st.session_state["authentication_status"]:
    authenticator.logout(button_name="SAIR", location="sidebar")
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
    

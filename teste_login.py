import streamlit as st

if not st.experimental_user.__dict__:
    if st.button("Log in"):
        st.login
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.keys}!")
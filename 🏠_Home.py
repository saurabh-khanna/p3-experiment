#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader

# st.set_page
st.set_page_config(
    page_title="S🎈nder",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# hiding the hamburger menu and footer
hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="collapsedControl"] {display: none;}
</style>

"""


# Main page

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("S🎈nder")
st.markdown("&nbsp;")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')

#st.write(stauth.Hasher(['abcdef', 'fedcba']).generate())

# Main page

if authentication_status:
    authenticator.logout('Logout', 'main')
    greeting = f'Welcome {name}!'
    st.markdown("&nbsp;")
    st.markdown('<p style="font-size: 24px;">' + str(greeting) + '</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 24px;">S🎈nder is an experimental internet search engine.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 24px;">You can use it to search the internet for anything, exactly like you would on Google.</p>', unsafe_allow_html=True)

    st.markdown("&nbsp;")

    started = st.button("Get started!")
    if started:
        switch_page("pretest")
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your Prolific ID as the username and your password to get started!')
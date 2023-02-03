#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="S🎈nder", page_icon=":candle:", layout="wide")

# hiding the hamburger menu and footer
hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

# Main page

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("S🎈nder")
st.markdown("&nbsp;")

st.markdown('<p style="font-size: 30px;">S🎈nder is an experimental Internet search engine.</p>', unsafe_allow_html=True)

st.markdown('<p style="font-size: 30px;">You can use it to search the Internet for anything, exactly like you would on Google.</p>', unsafe_allow_html=True)

st.markdown("&nbsp;")

started = st.button("Get started!")
if started:
    switch_page("pretest")
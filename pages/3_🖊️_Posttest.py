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

with st.form("pretest"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
       switch_page("treatment")
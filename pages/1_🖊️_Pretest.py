#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import random

st.set_page_config(
    page_title="S🎈nder",
    page_icon=":candle:",
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

st.markdown(
    '<p style="font-size: 24px;">Before you start using S🎈nder to browse the internet, please answer the following questions to the best of your ability.</p>',
    unsafe_allow_html=True,
)
st.write("&nbsp;")

with st.form("pretest"):
    gender = st.selectbox(
        "What gender do you identify as?", ["", "Male", "Female", "Other"]
    )
    st.write("&nbsp;")
    age = st.slider("What is you current age?", 0, 100, 50)
    st.write("&nbsp;")
    ethnicity = st.selectbox(
        "What is your ethnic background?",
        [
            "",
            "Caucasian",
            "African-American",
            "Latino or Hispanic",
            "Asian",
            "Native American",
            "Two or more ethnicities",
            "Other",
        ],
    )
    st.write("&nbsp;")
    education = st.selectbox(
        "What is your highest level of education?",
        ["", "High School", "Bachelor’s degree", "Master’s degree or above", "Other"],
    )
    st.write("&nbsp;")
    marital_status = st.selectbox(
        "What is your marital status?",
        ["", "Single", "Married", "Divorced", "Widowed", "Other"],
    )
    st.write("&nbsp;")
    household_income = st.selectbox(
        "What is your annual household income?",
        [
            "",
            "Less than $25,000",
            "$25,000 to $49,999",
            "$50,000 to $74,999",
            "$75,000 to $99,999",
            "$100,000 to $149,999",
            "$150,000 or more",
        ],
    )
    st.write("&nbsp;")
    domicile = st.selectbox(
        "Which of these best describes the general area where you live?",
        ["", "Urban", "Suburban", "Rural", "Other"],
    )
    st.write("&nbsp;")
    political_affiliation = st.selectbox(
        "What is your political affiliation?",
        ["", "Democrat", "Republican", "Independent", "Other"],
    )
    st.write("&nbsp;")
    religion = st.selectbox(
        "What is your religion?",
        ["", "Christian", "Jewish", "Muslim", "Hindu", "Buddhist", "Atheist", "Other"],
    )

    st.markdown("----")
    st.markdown("&nbsp;")

    st.warning(
        "Please rate your agreement or disagreement with the following statements."
    )
    st.markdown("&nbsp;")
    aot7_q1 = st.selectbox(
        "Allowing oneself to be convinced by an opposing argument is a sign of good character.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q2 = st.selectbox(
        "People should take into consideration evidence that goes against their beliefs.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q3 = st.selectbox(
        "People should revise their beliefs in response to new information or evidence.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q4 = st.selectbox(
        "Changing your mind is a sign of weakness.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q5 = st.selectbox(
        "Intuition is the best guide in making decisions.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q6 = st.selectbox(
        "It is important to persevere in your beliefs even when evidence is brought to bear against them.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )
    st.write("&nbsp;")
    aot7_q7 = st.selectbox(
        "One should disregard evidence that conflicts with one's established beliefs.",
        [
            "",
            "Disagree strongly",
            "Disagree moderately",
            "Disagree slightly",
            "Agree slightly",
            "Agree moderately",
            "Agree strongly",
        ],
    )

    st.markdown("----")
    st.markdown("&nbsp;")

    st.warning(
        "Please indicate the extent to which you feel positive or negative towards each issue mentioned below. Scores of 0 indicate greater negativity, and scores of 100 indicate greater positivity. Scores of 50 indicate that you feel neutral about the issue."
    )
    st.markdown("&nbsp;")
    secs_q1 = st.slider("Patriotism", 0, 100, 50)
    st.write("&nbsp;")
    secs_q2 = st.slider("Immigration", 0, 100, 50)
    st.write("&nbsp;")
    secs_q3 = st.slider("Abortion", 0, 100, 50)
    st.write("&nbsp;")
    secs_q4 = st.slider("Traditional Values", 0, 100, 50)
    st.write("&nbsp;")
    secs_q5 = st.slider("Gun Ownership", 0, 100, 50)
    st.write("&nbsp;")

    st.markdown("&nbsp;")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit answers and continue!")

    treatments = ["search1", "search2"]
    if submitted:
        switch_page(random.choice(treatments))
        # if '' in {gender, age, ethnicity, education, marital_status, household_income, domicile, political_affiliation, religion, aot7_q1, aot7_q2, aot7_q3, aot7_q4, aot7_q5, aot7_q6, aot7_q7, secs_q1, secs_q2, secs_q3, secs_q4, secs_q5}:
        #     st.error("Please answer all questions to proceed!")
        # else:
        #     switch_page("search1")

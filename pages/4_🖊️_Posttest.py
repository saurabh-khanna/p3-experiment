#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page

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
    '<p style="font-size: 24px;">Thanks your using S🎈nder to browse the internet. As a final step, please rate your agreement or disagreement with the following statements.</p>',
    unsafe_allow_html=True,
)
st.write("&nbsp;")

with st.form("pretest"):
    aot17_q1 = st.selectbox(
        "One should disregard evidence that conflicts with your established beliefs.",
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

    aot17_q2 = st.selectbox(
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

    aot17_q3 = st.selectbox(
        "Certain beliefs are just too important to abandon no matter how good a case can be made against them.",
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

    aot17_q4 = st.selectbox(
        "Beliefs should always be revised in response to new information or evidence.",
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

    aot17_q5 = st.selectbox(
        "People should always take into consideration evidence that goes against their beliefs.",
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

    aot17_q6 = st.selectbox(
        "I believe that loyalty to one's ideals and principles is more important than 'open-mindedness'.",
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

    aot17_q7 = st.selectbox(
        "I believe that the “new morality” of permissiveness is no morality at all.",
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

    aot17_q8 = st.selectbox(
        "Of all the different philosophies which exist in the world there is probably only one which is correct.",
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

    aot17_q9 = st.selectbox(
        "I think there are many wrong ways, but only one right way, to almost anything.",
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

    aot17_q10 = st.selectbox(
        "I believe letting youth hear controversial speakers can only confuse and mislead them.",
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

    aot17_q11 = st.selectbox(
        "I believe we should look to our religious authorities for decisions on moral issues.",
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

    aot17_q12 = st.selectbox(
        "I consider myself broad-minded and tolerant of other people's lifestyles.",
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

    aot17_q13 = st.selectbox(
        "A person should always consider new possibilities.",
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

    aot17_q14 = st.selectbox(
        "I believe that the different ideas of right and wrong that people in other societies have may be valid for them.",
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

    aot17_q15 = st.selectbox(
        "There are a number of people I have come to dislike because of the things they stand for.",
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

    aot17_q16 = st.selectbox(
        "I tend to classify people as either for me or against me.",
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

    aot17_q17 = st.selectbox(
        "I feel anger whenever a person stubbornly refuses to admit they are wrong.",
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
    secs_q1b = st.slider("Patriotism", 0, 100, 50)
    st.write("&nbsp;")
    secs_q2b = st.slider("Immigration", 0, 100, 50)
    st.write("&nbsp;")
    secs_q3b = st.slider("Abortion", 0, 100, 50)
    st.write("&nbsp;")
    secs_q4b = st.slider("Traditional Values", 0, 100, 50)
    st.write("&nbsp;")
    secs_q5b = st.slider("Gun Ownership", 0, 100, 50)
    st.write("&nbsp;")

    st.markdown("&nbsp;")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit answers and continue!")

    if submitted:
        if "" in {
            aot17_q1,
            aot17_q2,
            aot17_q3,
            aot17_q4,
            aot17_q5,
            aot17_q6,
            aot17_q7,
            aot17_q8,
            aot17_q9,
            aot17_q10,
            aot17_q11,
            aot17_q12,
            aot17_q13,
            aot17_q14,
            aot17_q15,
            aot17_q16,
            aot17_q17,
            secs_q1b,
            secs_q2b,
            secs_q3b,
            secs_q4b,
            secs_q5b,
        }:
            st.error("Please answer all questions to finish!")
        else:
            st.snow()
            st.success("Thank you for completing the survey!")

## PARAMETERS ##
import streamlit as st
from flask import copy_current_request_context
import numpy as np
import pandas as pd
from client import RestClient
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer, util
from streamlit_extras.switch_page_button import switch_page


@st.cache_data(show_spinner=False)
def fetch_data(query, _model):
    post_data = dict()
    post_data[len(post_data)] = dict(
        language_code="en", location_code=2840, keyword=query
    )
    response = client.post("/v3/serp/google/organic/live/regular", post_data)
    df = pd.DataFrame(response["tasks"][0]["result"][0]["items"])
    df.rename(columns={"content": "description"}, inplace=True)
    df.dropna(subset=["title", "description"], inplace=True)
    df.drop_duplicates(inplace=True)

    # clean domain
    df["domain"] = df.apply(lambda row: remove_prefix(str(row["domain"])), axis=1)
    
    # merge in pageranks
    # df = df.merge(
    #     pd.read_csv(Path("data/opr_top10milliondomains.csv"))[
    #         ["domain", "open_page_rank"]
    #     ],
    #     on=["domain"],
    #     how="left",
    # )
    # df["open_page_rank"] = df["open_page_rank"].fillna(0)
    df["open_page_rank"] = 1 # testing with fixed weights for now

    # all text for embeddings
    df["all_text"] = df["title"] + ". " + df["description"]

    # query_embedding = model.encode(query)
    df["result_embedding"] = df.apply(lambda row: model.encode(row["all_text"]), axis=1)
    
    result_vals = df['result_embedding'].values
    weight_vals = df['open_page_rank'].values
    df["growing_embedding"] = np.cumsum(result_vals * weight_vals) / np.cumsum(weight_vals)
    corpus_embedding = df["growing_embedding"].iloc[-1]

    df["representation"] = df.apply(
        lambda row: util.cos_sim(row["growing_embedding"], corpus_embedding).item(),
        axis=1,
    )
    
    df = df[["url", "title", "description", "representation"]]
    # st.write(df)
    return df


# Remove domain prefix
def remove_prefix(text, prefix="www."):
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


@st.cache_resource(show_spinner=False)
def load_model():
    # st.info("load_model running...")
    return SentenceTransformer("all-MiniLM-L6-v2")


#############
## CONTENT ##
#############

st.set_page_config(page_title="S🎈nder", page_icon=":candle:", layout="wide", initial_sidebar_state="collapsed")

# hiding the hamburger menu and footer
hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="collapsedControl"] {display: none;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("S🎈nder")
st.markdown("&nbsp;")

st.info(
    '''
    We want you to use our internet search platform to search for and browse information around these **5 topics**:

    1.	Patriotism in my country today
    2.	Openness to immigration
    3.	Abortion and its legal status
    4.	Traditional values in society today
    5.	Laws around gun ownership

    You can search for _anything_ related to these topics, and you can click on any results you like, exactly like you would on wesites like Google or Bing. You are also free to search results as many times as you want for each topic. Please spend roughly 8 to 10 minutes browsing the search results for each topic. **You are expected to spend 30 minutes in total using this search platform. Please click the button at the bottom of this page when you are finished.**
    ''')
st.write("&nbsp;")

col_a, col_b = st.columns([1, 3])

with col_a:
    st.markdown('You can start searching for information on the above topics using the textbox on the right.')
    st.write("&nbsp;")
    st.write("&nbsp;")
    st.markdown("You can also change the number of search results you want to see.")

with col_b:
    query = st.text_input("Type in your query and press ↩ to search.").lower().strip()
    st.write("&nbsp;")
    n_results = st.slider('Choose how many search results you want to see', 1, 100, 10)

if query != "":

    st.markdown("&nbsp;")

    with st.spinner("Getting your search results..."):

        model = load_model()
        client = RestClient(st.secrets["seo_username"], st.secrets["seo_password"])

        # demo
        if query in ["climate changez"]:
            df = pd.read_csv(Path("demo/" + query + ".csv"))
            metric = 0.5
        # default
        else:
            response = fetch_data(query, model)
            df = response

    col2, col1 = st.columns([1, 3])
    if n_results > len(df):
        n_results = len(df)
    df_print = df.head(n_results).copy()

    # df_print["final_rank"] = df_print.reset_index().index + 1

    with col1:
        st.markdown("### Search results")
        st.markdown("---")
        for index, row in df_print.iterrows():
            with st.container():
                if row["description"] == row["description"]:
                    st.markdown(
                        "> "
                        + row["url"]
                        + "<br/><br/><i>"
                        + row["title"]
                        + ".</i> "
                        + row["description"],
                        # + "<br/><br/>"
                        # + "Completeness: `"
                        # + str(round(row["representation"] * 100, 2))
                        # + "%`",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "> " + row["url"] + "<br/><br/>" + row["title"],
                        unsafe_allow_html=True,
                    )
                st.markdown("---")

    col2.markdown("### Completeness")
    col2.markdown("---")

    with col2:
        avg = round(df_print['representation'].iloc[n_results-1] * 100, 2) - 30
        st.write("How much information related to `" + str(query) + "` am I seeing?")
        st.metric(label="", value=str(avg) + "%")
        st.write("&nbsp;")
        st.info("S🎈nder gives you search results, and also tells you how _complete_ are these results. In other words, it shows you that " + str(avg) + "%" + " information related to `" + str(query) + "` on the internet is visible in the results on the right.")
        
st.markdown("&nbsp;")
st.markdown("&nbsp;")
st.markdown("&nbsp;")
st.markdown("&nbsp;")
st.markdown("&nbsp;")

if st.button("I have spent 30 minutes searching and want to move ahead!"):
    switch_page("posttest")
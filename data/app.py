import streamlit as st
import json
import pandas as pd

@st.cache(persist=True)
def load_data():
    with open('talca_cl.json') as json_file:
        data=json.load(json_file)
    lon=[float(d['x']) for d in data['nodes']]
    lat=[float(d['y']) for d in data['nodes']]
    node_name=[float(d['osmid']) for d in data['nodes']]
    df=pd.DataFrame({'latitude':lat,'longitude':lon,'id':node_name})
    return df

data = load_data()

st.title("Talca Ciclovias")
st.markdown("This application is a Streamlit dashboard that can be used "
            "to analyze motor vehicle collisions in NYC 🗽💥🚗")

st.header("Where are the most people injured in NYC?")
st.map(data)

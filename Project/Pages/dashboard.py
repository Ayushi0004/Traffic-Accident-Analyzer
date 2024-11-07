import streamlit as st 
import pandas as pd 
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go 

st.title("Traffic Accident Analyzer")

#load the dataset

df = pd.read_csv("Road.csv")

#display the dataset on the page
st.dataframe(df)

fig = px.sunburst(df, path=["Casualty_class", "Casualty_severity"], title="Casualty Class by Severity")
fig.show()

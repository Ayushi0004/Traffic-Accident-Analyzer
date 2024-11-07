import streamlit as st 
import pandas as pd 
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go 
st.markdown("<h1 style='color:white; font-weight:bolder; background-color:red; border:4px solid white; text-align:center;'>Traffic Accident Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='color:white; text-align:center; margin-top:20px;'>This project is for Analyizing India's Road Accidents between 2017 and 2022</h5>", unsafe_allow_html=True)
st.image('Assets/acc.jpeg',use_column_width=True)
st.markdown("<h3 style='color:white; text-align:center; '>About Detaset</h3>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'> The dataset, which includes manually recorded data on road traffic accidents in India from 2017 to 2022, has been processed meticulously to remove sensitive information through careful encoding. The final dataset comprises 32 attributes across 12,316 recorded accident cases. Preprocessing has prepared the data for analyzing key causes of accidents, with plans to use a range of machine learning classification algorithms for analysis. </p>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'> India experiences one of the world’s highest rates of road accidents, with over 150,000 fatalities annually. To understand and categorize road accidents in India, we can examine multiple factors like causes, vehicle types, accident types, and location details. </p>", unsafe_allow_html=True)


st.markdown("<h5 style='color:white; margin-top:20px;'>Causes:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>The main contributors to road accidents in India include reckless driving, speeding, impaired driving (such as alcohol influence), driver fatigue, substandard road conditions, and a lack of awareness regarding traffic rules and regulations.</p>", unsafe_allow_html=True)


st.markdown("<h5 style='color:white; margin-top:20px;'>Types of Vehicles:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Two-wheelers and four-wheelers account for most road accidents in India, though pedestrians and cyclists are also significantly affected.</p>", unsafe_allow_html=True)


st.markdown("<h5 style='color:white; margin-top:20px;'>Types of Accidents:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>The common accident types in India include head-on collisions, rear-end collisions, side-impact crashes, and rollovers.</p>", unsafe_allow_html=True)


st.markdown("<h5 style='color:white; margin-top:20px;'>Location:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Accidents occur across diverse locations, with the highest number reported on highways, followed by urban and rural roadways.</p>", unsafe_allow_html=True)

st.markdown("<h5 style='color:white; margin-top:20px;'>Classification:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Road accidents in India can be categorized into several main types. Vehicle-related accidents involve collisions between various vehicle types, such as cars, trucks, buses, and motorcycles. Pedestrian-related accidents involve pedestrians who either collide with vehicles or experience falls due to inadequate road infrastructure. Infrastructure-related accidents result from poor road conditions, including potholes, uneven surfaces, and insufficient lighting. Weather-related accidents are caused by adverse weather conditions like rain, fog, or snow, which impair visibility and affect vehicle control. Lastly, human error-related accidents occur due to human factors such as reckless driving, speeding, driving under the influence, or driver fatigue.</p>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>By examining and categorizing road accidents based on these factors, we can identify primary causes and implement effective prevention strategies. These may include infrastructure improvements, enhancing public awareness of traffic regulations, and enforcing stricter penalties for traffic violations. </p>", unsafe_allow_html=True)
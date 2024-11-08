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

st.sidebar.header("Filter Options")

#1 Create a bar chart for Accident Counts by Day of Week
st.subheader("Accident Counts by Day of Week")
fig = px.bar(df, x="Day_of_week", color="Day_of_week",
                title="Accident Counts by Day of Week",
                color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig)


#2 Create a pie chart by Distribution of Driver Age Groups
st.subheader("Distribution of Driver Age Groups")
fig = px.pie(df, names="Age_band_of_driver", title="Distribution of Driver Age Groups",
            color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)


#3 create a histogram chart by  Accidents by Driver's Gender
st.subheader("Accidents by Driver's Gender")
fig = px.histogram(df, x="Sex_of_driver", color="Sex_of_driver",
                    title="Accidents by Driver's Gender",
                    color_discrete_sequence=px.colors.diverging.Tealrose)
st.plotly_chart(fig)

#4 create a box chart by Accident Severity by Day of the Week
st.subheader("Accident Severity by Day of the Week")
fig = px.box(df, x="Day_of_week", y="Accident_severity", color="Day_of_week",
                title="Accident Severity by Day of the Week",
                color_discrete_sequence=px.colors.cyclical.Phase)
st.plotly_chart(fig)

#5 create a violin chart by Educational Level vs. Accident Severity
st.subheader("Educational Level vs. Accident Severity")
fig = px.violin(df, x="Educational_level", y="Accident_severity", color="Educational_level",
                title="Educational Level vs. Accident Severity",
                color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

#6 create a scatter chart by Accident Severity by Driving Experience
st.subheader("Accident Severity by Driving Experience")
fig = px.scatter(df, x="Driving_experience", y="Accident_severity", color="Driving_experience",
                    title="Accident Severity by Driving Experience",
                    color_discrete_sequence=px.colors.sequential.Sunset)
st.plotly_chart(fig)

#7 create a histogram chart by Vehicle Movement during Accidents
st.subheader("Vehicle Movement during Accidents")
fig = px.histogram(df, x="Vehicle_movement", color="Vehicle_movement",
                    title="Vehicle Movement during Accidents",
                    color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig)

#8 Create a line chart by Service Year of Vehicle and Accident Severity 
st.subheader("Service Year of Vehicle and Accident Severity")
fig = px.line(df, x="Service_year_of_vehicle", y="Accident_severity", color="Service_year_of_vehicle",
                title="Service Year of Vehicle and Accident Severity",
                color_discrete_sequence=px.colors.sequential.Inferno)
st.plotly_chart(fig)

#9 create a bar chart by Age Band of Casualty vs. Severity
st.subheader("Age Band of Casualty vs. Severity")
fig = px.bar(df, x="Age_band_of_casualty", y="Casualty_severity", color="Casualty_severity",
                title="Age Band of Casualty vs. Severity",
                color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig)

#10 create a bar chart by Fitness of Casualty and Accident Severity
st.subheader("Fitness of Casualty and Accident Severity")
fig = px.box(df, x="Fitness_of_casuality", y="Accident_severity", color="Fitness_of_casuality",
                title="Fitness of Casualty and Accident Severity",
                color_discrete_sequence=px.colors.qualitative.D3)
st.plotly_chart(fig)

#11 create a bar chart by Casualty Gender Distribution
st.subheader("Casualty Gender Distribution")
fig = px.pie(df, names="Sex_of_casualty", title="Casualty Gender Distribution",
            color_discrete_sequence=px.colors.sequential.Magma)
st.plotly_chart(fig)


#12 create a bar chart by Vehicle Type and Casualty Class
st.subheader("Vehicle Type and Casualty Class")
fig = px.histogram(df, x="Type_of_vehicle", color="Casualty_class",
                    title="Vehicle Type and Casualty Class",
                    color_discrete_sequence=px.colors.sequential.Teal)
st.plotly_chart(fig)

#13 create a bar chart by Accident Causes
st.subheader("Accident Causes")
fig = px.bar(df, x="Cause_of_accident", color="Cause_of_accident",
                title="Top Causes of Accidents",
                color_discrete_sequence=px.colors.qualitative.T10)
st.plotly_chart(fig)


#14 create a bar chart by Accidents by Vehicle Ownership

st.subheader("Accidents by Vehicle Ownership")
fig = px.pie(df, names="Owner_of_vehicle", title="Accidents by Vehicle Ownership",
                color_discrete_sequence=px.colors.sequential.Burg)
st.plotly_chart(fig)


#15 create a bar chart by Work of Casualty and Accident Severity

st.subheader("Work of Casualty and Accident Severity")
fig = px.box(df, x="Work_of_casuality", y="Accident_severity", color="Work_of_casuality",
                title="Work of Casualty and Accident Severity",
                color_discrete_sequence=px.colors.cyclical.Edge)
st.plotly_chart(fig)

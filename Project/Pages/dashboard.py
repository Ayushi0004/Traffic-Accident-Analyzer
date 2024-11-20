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
age_band_of_driver = st.sidebar.multiselect("Age Band of Driver", options=df['Age_band_of_driver'].unique())

#day of week
day_of_week = st.sidebar.multiselect("Day of Week", options=df['Day_of_week'].unique())

vehicles_involved = st.sidebar.slider("Number of Vehicles Involved", 
                                        min_value=int(df['Number_of_vehicles_involved'].min()), 
                                        max_value=int(df['Number_of_vehicles_involved'].max()), 
                                        value=(int(df['Number_of_vehicles_involved'].min()), int(df['Number_of_vehicles_involved'].max())))


# Apply filters to the dataset
filtered_data = df.copy()

if age_band_of_driver:
    filtered_data = filtered_data[filtered_data['Age_band_of_driver'].isin(age_band_of_driver)]

if day_of_week:
    filtered_data = filtered_data[filtered_data['Day_of_week'].isin(day_of_week)]


st.write("Filtered Data", filtered_data)

#1 Create a bar chart for Accident Counts by Day of Week
st.subheader("Accident Counts by Day of Week")
st.markdown("<p style='color:white;  margin-top:20px;'>The Accident Counts by Day of Week bar chart visualizes the frequency of accidents across the week, providing insights into which days might be more accident-prone. This analysis could reveal trends, such as higher accident rates during weekends or weekdays, likely due to varying traffic volumes and patterns. By identifying high-risk days, safety measures can be better scheduled to address peak traffic or high-risk periods.</p>", unsafe_allow_html=True)
fig = px.bar(df, x="Day_of_week", color="Day_of_week",
                title="Accident Counts by Day of Week",
                color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig)


#2 Create a pie chart by Distribution of Driver Age Groups
st.subheader("Distribution of Driver Age Groups")
st.markdown("<p style='color:white;  margin-top:20px;'>The Distribution of Driver Age Groups pie chart highlights which age groups are most involved in accidents, helping analysts understand demographic patterns in accident involvement. This information is valuable for targeting age-specific safety campaigns, as it reveals which age groups may benefit most from additional safety training or awareness programs.</p>", unsafe_allow_html=True)
fig = px.pie(df, names="Age_band_of_driver", title="Distribution of Driver Age Groups",
            color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)


#3 create a histogram chart by  Accidents by Driver's Gender
st.subheader("Accidents by Driver's Gender")
st.markdown("<p style='color:white; margin-top:20px;'>The Accidents by Driver's Gender histogram examines gender differences in accident occurrences. By visualizing accident counts for each gender, analysts can explore any disparities and determine if specific gender-targeted safety interventions are needed. This data is crucial in understanding whether gender-based factors influence accident rates, potentially guiding gender-focused road safety strategies.</p>", unsafe_allow_html=True)
fig = px.histogram(df, x="Sex_of_driver", color="Sex_of_driver",
                    title="Accidents by Driver's Gender",
                    color_discrete_sequence=px.colors.diverging.Tealrose)
st.plotly_chart(fig)

#4 create a box chart by Accident Severity by Day of the Week
st.subheader("Accident Severity by Day of the Week")
st.markdown("<p style='color:white;  margin-top:20px;'>The Accident Severity by Day of the Week box chart provides insight into how severe accidents tend to be on different days. This can reveal if certain days are associated with more serious incidents, possibly due to driver behavior, traffic density, or weekend fatigue. Such information supports targeted safety policies for days when accident severity tends to increase, focusing on mitigating risk factors.</p>", unsafe_allow_html=True)
fig = px.box(df, x="Day_of_week", y="Accident_severity", color="Day_of_week",
                title="Accident Severity by Day of the Week",
                color_discrete_sequence=px.colors.cyclical.Phase)
st.plotly_chart(fig)

#5 create a violin chart by Educational Level vs. Accident Severity
st.subheader("Educational Level vs. Accident Severity")
st.markdown("<p style='color:white;  margin-top:20px;'>The Educational Level vs. Accident Severity violin chart visualizes the potential correlation between a driver’s educational background and the severity of accidents they are involved in. By analyzing this data, one can assess whether different education levels impact road safety awareness, guiding the development of targeted educational resources or awareness programs for specific demographics.</p>", unsafe_allow_html=True)
fig = px.violin(df, x="Educational_level", y="Accident_severity", color="Educational_level",
                title="Educational Level vs. Accident Severity",
                color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

#6 create a scatter chart by Accident Severity by Driving Experience
st.subheader("Accident Severity by Driving Experience")
st.markdown("<p style='color:white;  margin-top:20px;'>The Accident Severity by Driving Experience scatter chart displays accident severity in relation to the driver’s experience. This allows analysts to evaluate whether less experienced drivers are more likely to be involved in severe accidents, potentially highlighting the need for advanced training programs for newer drivers or additional support for novice drivers.</p>", unsafe_allow_html=True)
fig = px.scatter(df, x="Driving_experience", y="Accident_severity", color="Driving_experience",
                    title="Accident Severity by Driving Experience",
                    color_discrete_sequence=px.colors.sequential.Sunset)
st.plotly_chart(fig)

#7 create a histogram chart by Vehicle Movement during Accidents
st.subheader("Vehicle Movement during Accidents")
st.markdown("<p style='color:white; margin-top:20px;'>The Vehicle Movement during Accidents histogram breaks down accident occurrences based on the type of vehicle movement involved, offering insights into how certain maneuvers contribute to accident rates. By understanding which movements are frequently associated with accidents, traffic authorities can implement policies and education programs to promote safer driving practices, especially during high-risk maneuvers.</p>", unsafe_allow_html=True)
fig = px.histogram(df, x="Vehicle_movement", color="Vehicle_movement",
                    title="Vehicle Movement during Accidents",
                    color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig)

#8 Create a line chart by Service Year of Vehicle and Accident Severity 
st.subheader("Service Year of Vehicle and Accident Severity")
st.markdown("<p style='color:white;  margin-top:20px;'>The Service Year of Vehicle and Accident Severity line chart explores the relationship between the vehicle’s age and the severity of accidents. This analysis can reveal if older vehicles are more prone to serious accidents, possibly due to outdated safety features or increased wear. Such findings can advocate for regular vehicle checks and regulations for older vehicles to ensure they meet safety standards.</p>", unsafe_allow_html=True)
fig = px.line(df, x="Service_year_of_vehicle", y="Accident_severity", color="Service_year_of_vehicle",
                title="Service Year of Vehicle and Accident Severity",
                color_discrete_sequence=px.colors.sequential.Inferno)
st.plotly_chart(fig)

#9 create a bar chart by Age Band of Casualty vs. Severity
st.subheader("Age Band of Casualty vs. Severity")
st.markdown("<h5 style='color:white;  margin-top:20px;'>The Age Band of Casualty vs. Severity bar chart shows how casualty severity varies by age group, which is essential for identifying vulnerable age groups more susceptible to severe injuries. These insights can drive age-specific safety campaigns or health initiatives, ensuring that high-risk age bands receive focused attention to reduce severe injuries.</h5>", unsafe_allow_html=True)
fig = px.bar(df, x="Age_band_of_casualty", y="Casualty_severity", color="Casualty_severity",
                title="Age Band of Casualty vs. Severity",
                color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig)

#10 create a bar chart by Fitness of Casualty and Accident Severity
st.subheader("Fitness of Casualty and Accident Severity")
st.markdown("<p style='color:white;  margin-top:20px;'>The Fitness of Casualty and Accident Severity box chart evaluates if a casualty’s fitness level correlates with accident severity, potentially indicating that physical health might influence injury outcomes. This can provide a basis for promoting physical fitness as a preventative measure for severe injuries, particularly for those in demographics prone to accidents.</p>", unsafe_allow_html=True)
fig = px.box(df, x="Fitness_of_casuality", y="Accident_severity", color="Fitness_of_casuality",
                title="Fitness of Casualty and Accident Severity",
                color_discrete_sequence=px.colors.qualitative.D3)
st.plotly_chart(fig)

#11 create a bar chart by Casualty Gender Distribution
st.subheader("Casualty Gender Distribution")
st.markdown("<p style='color:white;  margin-top:20px;'>The Casualty Gender Distribution pie chart highlights gender distribution among accident casualties, showing which gender is more frequently affected. Understanding this distribution aids in creating gender-focused safety campaigns, tailoring messages or interventions to reduce casualty rates for the more affected gender, thereby enhancing overall road safety.</p>", unsafe_allow_html=True)
fig = px.pie(df, names="Sex_of_casualty", title="Casualty Gender Distribution",
            color_discrete_sequence=px.colors.sequential.Magma)
st.plotly_chart(fig)


#12 create a bar chart by Vehicle Type and Casualty Class
st.subheader("Vehicle Type and Casualty Class")
st.markdown("<p style='color:white;  margin-top:20px;'>The Vehicle Type and Casualty Class histogram examines which types of vehicles are more associated with specific classes of casualties, offering insight into the risk levels of various vehicle types. By understanding these relationships, policymakers can implement vehicle-specific guidelines or safety standards to reduce accident severity for high-risk vehicle categories.</p>", unsafe_allow_html=True)
fig = px.histogram(df, x="Type_of_vehicle", color="Casualty_class",
                    title="Vehicle Type and Casualty Class",
                    color_discrete_sequence=px.colors.sequential.Teal)
st.plotly_chart(fig)

#13 create a bar chart by Accident Causes
st.subheader("Accident Causes")
st.markdown("<p style='color:white;  margin-top:20px;'>The Top Causes of Accidents bar chart reveals the primary causes of accidents, essential for pinpointing root factors behind incidents. By highlighting common causes, authorities can develop targeted interventions, such as awareness campaigns and regulations to address the most significant accident causes, thereby enhancing road safety.</p>", unsafe_allow_html=True)
fig = px.bar(df, x="Cause_of_accident", color="Cause_of_accident",
                title="Top Causes of Accidents",
                color_discrete_sequence=px.colors.qualitative.T10)
st.plotly_chart(fig)


#14 create a bar chart by Accidents by Vehicle Ownership

st.subheader("Accidents by Vehicle Ownership")
st.markdown("<p style='color:white; margin-top:20px;'>The Accidents by Vehicle Ownership pie chart explores whether vehicle ownership affects accident involvement, which could indicate differing caution levels between owners and non-owners. This insight can inform policies encouraging responsible driving habits among all drivers, potentially reducing accident rates among non-owners who may drive differently.</p>", unsafe_allow_html=True)
fig = px.pie(df, names="Owner_of_vehicle", title="Accidents by Vehicle Ownership",
                color_discrete_sequence=px.colors.sequential.Burg)
st.plotly_chart(fig)


#15 create a bar chart by Work of Casualty and Accident Severity

st.subheader("Work of Casualty and Accident Severity")
st.markdown("<p style='color:white;  margin-top:20px;'>The Work of Casualty and Accident Severity box chart assesses whether a casualty’s occupation impacts accident severity, potentially hinting at work-related stress or fatigue. This data can guide occupational health and safety policies, focusing on promoting road safety among workers in high-stress or high-risk jobs where accident severity may be greater.</p>", unsafe_allow_html=True)
fig = px.box(df, x="Work_of_casuality", y="Accident_severity", color="Work_of_casuality",
                title="Work of Casualty and Accident Severity",
                color_discrete_sequence=px.colors.cyclical.Edge)
st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, I am Jin, welcome to my application!')
st.write('Dataset des voitures')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)
df_voiture


option_region = st.radio( "Select region",
                 ('Japan', 'USA', 'Europe'))

if option_region == 'USA':
    df1 = df_voiture.loc[df_voiture["continent"] ==" US."]
    df1
    st.line_chart(df1['mpg'])
    viz_correlation=sns.heatmap(df1.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    
if option_region == 'Europe':
    df2 = df_voiture.loc[df_voiture["continent"] ==" Europe."]
    df2
    st.line_chart(df2['mpg'])
    viz_correlation=sns.heatmap(df2.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    
else:
    df3 = df_voiture.loc[df_voiture["continent"] ==" Japan."]
    df3
    st.line_chart(df3['mpg'])
    viz_correlation=sns.heatmap(df3.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    











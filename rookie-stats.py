import pandas as pd
import streamlit as st

URL = "https://raw.githubusercontent.com/Brevon1104/dsc205/main/NBA%20data"
df=pd.read_csv(URL)

df.set_index('Player', inplace=True)

st.title('NBA Rookie of the Year Stats')

selected_columns = ['FG%', '3P%', 'FT%', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK']
df_selected = df[selected_columns]

st.sidebar.title('Select Stat to Filter By')
statistic = st.sidebar.radio('Choose a Statistic', df_selected.columns)

statistic_df = df[[statistic]]

statistic_mean = statistic_df.mean().iloc[0]
above_average_df = statistic_df[statistic_df[statistic] > statistic_mean]

st.write('## Sorted DataFrame based on', statistic)
st.bar_chart(above_average_df)

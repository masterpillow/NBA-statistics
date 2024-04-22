import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
csv_file_path = '/path_to_your_file/2023-2024 NBA Player Stats_exported.csv'
df = pd.read_csv(csv_file_path)

# Extract a list of unique teams from the DataFrame
teams = df['Tm'].unique().tolist()
teams.sort()  # Sort teams alphabetically

# Dropdown for team selection
selected_teams = st.multiselect('Select teams to compare:', teams)

# Dropdown for metric selection
metrics = ['Offensive Rating', 'Defensive Rating']
selected_metric = st.selectbox('Select metric to compare:', metrics)

# Filter the DataFrame based on the selected teams
filtered_df = df[df['Tm'].isin(selected_teams)]

if selected_metric == 'Offensive Rating':
    # For simplicity, using 'PTS' as offensive rating
    metric_df = filtered_df.groupby('Tm')['PTS'].sum().reset_index()
    metric_label = 'Total Points'
elif selected_metric == 'Defensive Rating':
    # For simplicity, using 'STL' + 'BLK' as defensive rating
    # Adjust this calculation based on your defensive metric
    metric_df = filtered_df.groupby('Tm').apply(lambda x: (x['STL'] + x['BLK']).sum()).reset_index(name='Def_Rating')
    metric_df.columns = ['Tm', 'Def_Rating']  # Rename columns for clarity
    metric_label = 'Defensive Rating'

# Plotting with Plotly
fig = px.bar(metric_df, x='Tm', y=metric_df.columns[1], 
             labels={'x': 'Teams', 'y': metric_label},
             title=f'Comparison of {selected_metric} by Selected Teams')
st.plotly_chart(fig)

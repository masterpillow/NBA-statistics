import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '2023-2024 NBA Player Stats_exported.csv'
df = pd.read_csv(csv_file_path)

df['Offensive_Rating'] = df['PTS'] 


df['Defensive_Rating'] = df['STL'] + df['BLK'] 


team_ratings = df.groupby('Tm').agg({
    'Offensive_Rating': 'mean', 
    'Defensive_Rating': 'mean',
}).reset_index()

# Dropdown for team selection
teams = team_ratings['Tm'].unique().tolist()
selected_teams = st.multiselect('Select teams to compare:', teams)

# Filter for selected teams
selected_team_ratings = team_ratings[team_ratings['Tm'].isin(selected_teams)]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35  # Width of the bars
indices = range(len(selected_team_ratings))  # Team indices

ax.bar(indices, selected_team_ratings['Offensive_Rating'], width, label='Offensive Rating')
ax.bar([i + width for i in indices], selected_team_ratings['Defensive_Rating'], width, label='Defensive Rating')

ax.set_xlabel('Teams')
ax.set_ylabel('Rating')
ax.set_title('Team Offensive and Defensive Ratings')
ax.set_xticks([i + width / 2 for i in indices])
ax.set_xticklabels(selected_team_ratings['Tm'])
ax.legend()

st.pyplot(fig)

    st.error(f"An error occurred: {e}")


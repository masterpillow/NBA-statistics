import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
try:
    csv_file_path = '2023-2024 NBA Player Stats_exported.csv'
    df = pd.read_csv(csv_file_path)
    
    # Ensure necessary columns are present
    expected_columns = ['TmPoss', 'OppPoss', 'OppPts', 'PTS', 'Tm']
    if not all(col in df.columns for col in expected_columns):
        st.error("Error: One or more required columns are missing from the dataset.")
        st.stop()
    
    # Calculate Offensive and Defensive Ratings
    df['OR'] = 100 * df['PTS'] / (df['TmPoss'] + df['OppPoss'])
    df['DR'] = 100 * df['OppPts'] / (df['TmPoss'] + df['OppPoss'])

    # Aggregate to team level for visualization
    team_ratings = df.groupby('Tm').agg({
        'OR': 'mean',  # Using mean here, but you might choose max, min, or another method
        'DR': 'mean',
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

    ax.bar(indices, selected_team_ratings['OR'], width, label='Offensive Rating')
    ax.bar([i + width for i in indices], selected_team_ratings['DR'], width, label='Defensive Rating')

    ax.set_xlabel('Teams')
    ax.set_ylabel('Rating')
    ax.set_title('Team Offensive and Defensive Ratings')
    ax.set_xticks([i + width / 2 for i in indices])
    ax.set_xticklabels(selected_team_ratings['Tm'])
    ax.legend()

    st.pyplot(fig)
except Exception as e:
    st.error(f"An error occurred: {e}")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    csv_file_path = '2023-2024 NBA Player Stats_exported.csv'
    df = pd.read_csv(csv_file_path)
    df['Offensive_Rating'] = df['PTS']  # Assuming PTS is points scored which are used for offensive rating
    df['Defensive_Rating'] = df['STL'] + df['BLK']  # Sum of steals and blocks for defensive rating
    return df

def calculate_team_ratings(df):
    return df.groupby('Tm').agg({
        'Offensive_Rating': 'mean', 
        'Defensive_Rating': 'mean'
    }).reset_index()

def plot_ratings(data, selected_teams):
    # Filter for selected teams
    selected_team_ratings = data[data['Tm'].isin(selected_teams)]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.35  # Width of the bars
    indices = list(range(len(selected_team_ratings)))  # Team indices

    ax.bar(indices, selected_team_ratings['Offensive_Rating'], width, label='Offensive Rating')
    ax.bar([i + width for i in indices], selected_team_ratings['Defensive_Rating'], width, label='Defensive Rating')

    ax.set_xlabel('Teams')
    ax.set_ylabel('Rating')
    ax.set_title('Team Offensive and Defensive Ratings')
    ax.set_xticks([i + width / 2 for i in indices])
    ax.set_xticklabels(selected_team_ratings['Tm'])
    ax.legend()

    st.pyplot(fig)

def main():
    df = load_data()
    team_ratings = calculate_team_ratings(df)

    # Dropdown for team selection
    teams = team_ratings['Tm'].unique().tolist()
    selected_teams = st.multiselect('Select teams to compare:', teams)

    if selected_teams:
        plot_ratings(team_ratings, selected_teams)
    else:
        st.write("Select one or more teams to display ratings.")

if __name__ == "__main__":
    main()

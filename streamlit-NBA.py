import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # Load the data from a CSV file
    csv_file_path = '2023-2024 NBA Player Stats_exported.csv'
    df = pd.read_csv(csv_file_path)
    # Calculate ratings
    df['Offensive_Rating'] = df['PTS']  # Assume PTS is the offensive rating
    df['Defensive_Rating'] = df['STL'] + df['BLK']  # Sum of steals and blocks as the defensive rating
    return df

def calculate_team_ratings(df):
    # Group by team and calculate mean ratings
    return df.groupby('Tm').agg({
        'Offensive_Rating': 'mean', 
        'Defensive_Rating': 'mean'
    }).reset_index()

def plot_ratings(data, selected_teams, rating_type):
    # Filter data for selected teams
    filtered_data = data[data['Tm'].isin(selected_teams)]
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    team_indices = range(len(filtered_data))  # Team indices
    ax.bar(team_indices, filtered_data[rating_type], color='blue', label=rating_type)

    ax.set_xlabel('Teams')
    ax.set_ylabel('Rating')
    ax.set_title(f'Team {rating_type}')
    ax.set_xticks(team_indices)
    ax.set_xticklabels(filtered_data['Tm'])
    ax.legend()

    st.pyplot(fig)

def main():
    df = load_data()
    team_ratings = calculate_team_ratings(df)

    # Dropdown to select teams
    teams = team_ratings['Tm'].unique().tolist()
    selected_teams = st.multiselect('Select teams to compare:', teams, default=teams)

    # Dropdown to select rating type
    rating_types = ['Offensive_Rating', 'Defensive_Rating']
    selected_rating_type = st.selectbox('Select rating type:', rating_types)

    if selected_teams:
        plot_ratings(team_ratings, selected_teams, selected_rating_type)
    else:
        st.write("Select one or more teams to display ratings.")

if __name__ == "__main__":
    main()

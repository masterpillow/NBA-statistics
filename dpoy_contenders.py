import streamlit as st
import pandas as pd

# Load data function
@st.cache
def load_data():
    data_path = '2023-2024 NBA Player Stats_exported.csv'
    data = pd.read_csv(data_path)
    return data

def main():
    st.title('NBA Defensive Player of the Year (DPOY) Contenders')
    df = load_data()
    
    # Calculate a defensive score perhaps as a simple sum of key defensive stats
    df['Defensive Score'] = df['BLK'] + df['STL'] + df['DRB'] + 0.5 * df['TRB']
    
    # Get top 3 DPOY contenders based on defensive score
    top_defenders = df.sort_values('Defensive Score', ascending=False).head(3)
    
    st.write("Top 3 DPOY Contenders based on Defensive Statistics:")
    st.dataframe(top_defenders[['Player', 'Tm', 'BLK', 'STL', 'DRB', 'TRB', 'Defensive Score']])
    
    # Show some basic stats in a nicer format
    for index, player in top_defenders.iterrows():
        st.subheader(f"{player['Player']} ({player['Tm']})")
        st.text(f"Blocks: {player['BLK']}, Steals: {player['STL']}, Defensive Rebounds: {player['DRB']}, Total Rebounds: {player['TRB']}")

if __name__ == "__main__":
    main()

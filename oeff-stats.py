import pandas as pd
import streamlit as st

URL = "https://raw.githubusercontent.com/Brevon1104/dsc205/main/2023-2024%20NBA%20Player%20Stats%20-%20Regular.csv"
df = pd.read_csv(URL)

URL2 = "https://raw.githubusercontent.com/Brevon1104/dsc205/main/NBA%20Stats%20202324%20Team%20Metrics%20Away-Home-Last%205%20Splits.csv"
df2 = pd.read_csv(URL2)

df.rename(columns={'Tm': 'TEAM'}, inplace=True)

team_3p_pct = df.groupby('TEAM')['3P%'].mean().reset_index()
team_3p_pct.fillna(0, inplace=True)

team_oEFF = df2.groupby('TEAM')['oEFF'].mean().reset_index()

team_stats = pd.merge(team_3p_pct, team_oEFF, on='TEAM')

team_stats.set_index('TEAM', inplace=True)

st.write("3P% vs oEFF for NBA Teams")
scatter_chart = st.scatter_chart(team_stats, x='3P%', y='oEFF')



import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
conn = sqlite3.connect("Database/bce.db")
c = conn.cursor()

st.title('Get precentage of Jur')
df = pd.read_sql_query("SELECT JuridicalForm FROM enterprise", conn)
chart_data = pd.DataFrame(df["JuridicalForm"].value_counts(normalize=True, sort = True) * 100).reset_index()
chart_data.rename({'index': 'JuridicalForm', 'JuridicalForm': 'Percentage'}, axis=1, inplace=True)
chart_data_greatest = chart_data[chart_data["Percentage"] > 1]
c = alt.Chart(chart_data_greatest).mark_bar().encode(
    x=alt.X('JuridicalForm', sort=None),
    y='Percentage',
)

st.altair_chart(c, use_container_width=True)
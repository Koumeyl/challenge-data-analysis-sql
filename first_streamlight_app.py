import streamlit as st
import pandas as pd
import altair as alt
import sqlite3

from case_three import percentage_of_companies_per_type
conn = sqlite3.connect("Database/bce.db")
c = conn.cursor()

st.title('Get precentage of JuridicalForm')
df = pd.read_sql_query("SELECT JuridicalForm FROM enterprise", conn)
chart_data = pd.DataFrame(df["JuridicalForm"].value_counts(normalize=True, sort = True, dropna=False) * 100).reset_index()
chart_data.rename({'index': 'JuridicalForm', 'JuridicalForm': 'Percentage'}, axis=1, inplace=True)
c = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('JuridicalForm', sort=None),
    y='Percentage',
)
st.altair_chart(c, use_container_width=True)

# percentage_of_companies_per_type(conn)

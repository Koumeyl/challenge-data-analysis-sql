import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
import numpy as np
from case_three import percentage_of_companies_per_type
conn = sqlite3.connect("Database/bce.db")
c = conn.cursor()

st.title('Get precentage of JuridicalForm')
st.sidebar.header('Select what to display')
df = pd.read_sql_query("""Select JuridicalForm from enterprise
""", conn)

df_description = pd.read_sql_query("""select description, code from code
where code.Language = "FR"
""", conn)
conn.close()
df_count = pd.DataFrame(df["JuridicalForm"].value_counts(normalize=True, sort = True, dropna=False) * 100).reset_index()

df_count.rename({'index': 'JuridicalForm', 'JuridicalForm': 'Percentage'}, axis=1, inplace=True)
chart_data = pd.merge(df_count, df_description, left_on="JuridicalForm", right_on="Code", how="left")


col_list = chart_data['Percentage'].values.tolist()
values = st.slider(
    'Select a range of values',
    0.01,
    chart_data['Percentage'].max().item(), (0.01, chart_data['Percentage'].max().item()))
st.write(chart_data['Percentage'].min(skipna = False).item())





chart_data = chart_data[chart_data['Percentage'].between(values[0],values[1])]
c = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('Description', sort=None),
    y='Percentage'
)


# text = c.mark_text(
#     align='left',
#     baseline='middle',
#     dx=3  # Nudges text to right so it doesn't appear on top of the bar
# ).encode(
#     text=chart_data['Code']
# )
st.altair_chart(c, use_container_width=True)

# percentage_of_companies_per_type(conn)

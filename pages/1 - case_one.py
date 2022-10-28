import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import sqlite3
conn = sqlite3.connect("Database/bce.db")
c = conn.cursor()





def case_one_data(conn):
    df = pd.read_sql_query("""Select JuridicalForm from enterprise
    """, conn)

    df_description = pd.read_sql_query("""select description, code from code
    where code.Language = "FR"
    """, conn)
    
    df_count = pd.DataFrame(df["JuridicalForm"].value_counts(normalize=True, sort = True, dropna=False) * 100).reset_index()

    df_count.rename({'index': 'JuridicalForm', 'JuridicalForm': 'Percentage'}, axis=1, inplace=True)
    chart_data = pd.merge(df_count, df_description, left_on="JuridicalForm", right_on="Code", how="left")
    chart_data["Description"].fillna("Juridical form not available",  inplace = True)
    return chart_data

def case_one_display(chart_data):
    number_min = st.number_input('Insert minimum number', min_value= 0.01, max_value= 41.00, value=0.01)
    number_max = st.number_input('Insert maximum number', min_value= 0.01, max_value= 41.00, value = 41.00)
    chart_data = chart_data[chart_data['Percentage'].between(number_min,number_max)]
    fig = px.bar(chart_data, x='Description', y='Percentage', text_auto='.3s', title='Percentage of companies per juridical form')
    st.plotly_chart(fig, use_container_width=True)

st.title('Get precentage of companies per juridical form')
with st.container():
    with st.spinner('Rendering the display'):
        case_one_display(case_one_data(conn))
    st.success('Done!')

conn.close()
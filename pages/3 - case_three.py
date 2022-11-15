import pandas as pd
import plotly.express as px
import streamlit as st
import sqlite3

conn = sqlite3.connect("Database/bce.db")
c = conn.cursor()



def case_three_data(conn):
    df = pd.read_sql_query("SELECT TypeOfEnterprise FROM enterprise", conn)

    df_description = pd.read_sql_query("""select description, Code
    from code
    where code.Category = "TypeOfEnterprise" and Language = "FR"
    """, conn)

    df = pd.DataFrame(df["TypeOfEnterprise"].value_counts(normalize=True, sort = True) * 100).reset_index()
    df.rename({'TypeOfEnterprise': 'Percentage', 'index': 'TypeOfEnterprise'}, axis=1, inplace=True)
    #Personne morale ou Personne physique
    df = pd.merge(df, df_description, left_on="TypeOfEnterprise", right_on="Code", how="left", suffixes=('', '_drop'))
    return df

def case_three_display(chart_data):
    
    fig = px.pie(chart_data,values='Percentage', names='Description')
    fig.update_layout(width=700, height=700, font=dict(size=18))
    st.plotly_chart(fig, use_container_width=True)

st.image("https://economie.fgov.be/themes/custom/economie_theme/images/logo-en.svg", width=100)
st.title('Get precentage of each type of companies')
with st.spinner('Rendering the display'):
    case_three_display(case_three_data(conn))


conn.close()
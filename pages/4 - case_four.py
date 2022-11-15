import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

#con = sqlite3.connect("bce")

#def case_four_data():
#    df = pd.read_csv("yo.csv")
#    tst = df.groupby('NaceCode')
#    dft = tst.mean('age').reset_index()
#    df['age'] = dft['NaceCode'].astype('str')
#    return (dft)

def case_four_display(chart_data):
    number_min = st.number_input('Insert minimum age', min_value= 0.00, max_value= 100.00, value=0.00)
    number_max = st.number_input('Insert maximum age', min_value= 0.00, max_value= 100.00, value = 100.00)
    chart_data = chart_data[chart_data['age'].between(number_min,number_max)]
    fig = px.bar(chart_data, x='Description', y='age', text_auto='.3s', title='Average age for each NaceCode')
    fig.update_layout(font=dict(size=15))
    st.plotly_chart(fig, use_container_width=True)

#yo = case_four_data()
st.image("https://economie.fgov.be/themes/custom/economie_theme/images/logo-en.svg", width=100)
st.title("Average age of each company per sector")
case_four_display(pd.read_csv('age.csv').sort_values('age', ascending=False))
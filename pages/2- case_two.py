
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def get_company_status():
    fig = go.Figure(data=[go.Pie(labels=['striking','Actif','?'], values=[25827,1863292,1581446],hole=0.4)])
    fig.update_layout(width=700, height=700, font=dict(size=18))
    st.plotly_chart(fig, use_container_width=True)
    # print(df_status["strike_count"].idxmax())

st.image("https://economie.fgov.be/themes/custom/economie_theme/images/logo-en.svg", width=100)
st.title('Get precentage of companies under each status')
get_company_status()
from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
import altair as alt
import sqlite3
import numpy as np
import plotly.express as px


st.set_page_config(layout="wide")
st.image("https://economie.fgov.be/themes/custom/economie_theme/images/logo-en.svg", width=1000)
st.title("Case study on the active companies in Belgium referenced on the public open data")
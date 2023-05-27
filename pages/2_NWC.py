import streamlit as st

st.title("Net Working Capital")
import sys
sys.path.append('https://github.com/GurminSingh/Streamlit.git')  # Replace 'path/to/directory' with the actual path

from Valuation import combined_df

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64

def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x


df1 = pd.DataFrame(combined_df)
df1 = df1.reset_index()
df1.columns = ['Index'] + list(df1.columns[1:])

df11=combined_df
df11 = df11.applymap(format_float)
df11.columns = ['2017', '2018', '2019','2020','2021','2022','2023','2024','2025','2026','2027','2028']

# Reset the index of the DataFrame to make it unique



st.table(df11)

y_value = st.selectbox('Choisir la valeur y', df1['Index'].unique())
x_values = df11.columns[0:]
y_values = df1.loc[df1['Index'] == y_value].values[0][1:]
fig = go.Figure()
fig.add_trace(go.Bar(x=x_values, y=y_values, marker_color='#0a7ed1'))
fig.update_layout(title=y_value, xaxis_title='', yaxis_title='')
st.plotly_chart(fig)

from Valuation import M

def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

df11=M
df11 = M.applymap(format_float)
df11.columns = ['2017', '2018', '2019','2020','2021','2022','Average','Median','Last Value']

st.table(df11)








import streamlit as st

st.title("FCFF")
import sys
sys.path.append('/Users/gavysingh/Downloads/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path

from Valuation import FCFF_df

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


df1 = pd.DataFrame(FCFF_df)
df1 = df1.reset_index()
df1.columns = ['Index'] + list(df1.columns[1:])

df11=FCFF_df
df11 = df11.applymap(format_float)
df11.columns = ['2017', '2018', '2019','2020','2021','2022']
import streamlit as st
import pandas as pd


# Display the styled table
st.table(df11)


y_value = st.selectbox('Choisir la valeur y', df1['Index'].unique())
x_values = df11.columns[0:]
y_values = df1.loc[df1['Index'] == y_value].values[0][1:]
fig = go.Figure()
fig.add_trace(go.Bar(x=x_values, y=y_values, marker_color='#0a7ed1'))
fig.update_layout(title=y_value, xaxis_title='', yaxis_title='')
st.plotly_chart(fig)







import streamlit as st

st.title("Produit")
import sys
sys.path.append('https://github.com/GurminSingh/Streamlit.git')  # Replace 'path/to/directory' with the actual path

from Valuation import Assumption_revenues_df

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


df3 = pd.DataFrame(Assumption_revenues_df)
df3 = df3.reset_index()
df3.columns = ['Index'] + list(df3.columns[1:])
df33=Assumption_revenues_df
df33 = df33.applymap(format_float)




import streamlit as st
import pandas as pd


st.table(df33)
Assumption_revenues_df = Assumption_revenues_df.T
melted_df = pd.melt(Assumption_revenues_df, ignore_index=False, var_name='Product', value_name='Sales')
melted_df.reset_index(inplace=True)
melted_df.rename(columns={'index': 'Year'}, inplace=True)
    # Filter out 'Total Sales' rows
melted_df = melted_df[melted_df['Product'] != 'Total']
labels = {
    'Year': 'Year',
    'Product': 'Product',
    'Sales': 'Sales (in millions)',}
color_scale = 'Blues'
fig = px.sunburst(melted_df, path=['Year', 'Product'], values='Sales', color='Sales',
                  color_continuous_scale=color_scale, hover_name='Year', labels=labels,
                  branchvalues='total', title='Revenues by Year and Product')
st.plotly_chart(fig)





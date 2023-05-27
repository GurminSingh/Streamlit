import streamlit as st

st.title("Cost of Debt")
import sys
sys.path.append('/Users/gavysingh/Downloads/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path

from Valuation import df, ratio, spread,total_debt,w_avg_maturity,cost_of_debt,debts,mv_debt,rf

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



df6=df



total_debt = "{:.1f} M€".format(total_debt / 1_000)

w_avg_maturity = round(w_avg_maturity, 2)
cost_of_debt = cost_of_debt * 100
cost_of_debt = f"{cost_of_debt:.2f}%"
ratio="{:.1f}".format(ratio)
spread = spread * 100
spread = f"{spread:.2f}%"
mv_debt = "{:.1f} M€".format(mv_debt / 1e6)
rf = rf * 100
rf = f"{rf:.2f}%"

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)


st.subheader('The risk free rate')

st.metric("The risk free rate of Belgium", rf)


st.subheader('The Default Spread')
st.table(df6)
col1, col2 = st.columns(2)
col1.metric("Interest Coverage ratio", ratio)
col2.metric("The Default Spread" ,spread)

st.subheader('The Market value of debt')
import streamlit as st

df = pd.DataFrame(debts, columns=['Year', 'Debt'])
st.table(df)
col1, col2, col3,col4 = st.columns(4)
col1.metric("Total Debt", total_debt)
col2.metric("Weight to maturity", w_avg_maturity)
col3.metric("Market value of debt", mv_debt)
col4.metric("Cost of debt", cost_of_debt)

ColourWidgetText(cost_of_debt, '#0a7ed1')   


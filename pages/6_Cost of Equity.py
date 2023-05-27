import streamlit as st

st.title("Cost of Debt")
import sys
sys.path.append('/Users/gavysingh/Downloads/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path

from Valuation import erp,shares_outstanding,Current_Share_Price,definitive_coef_0,definitive_coef_2,stati_mean_SMB,marketCap,definitive_coef_1,stati_mean_HML,cost_of_equity
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




erp = erp * 100
erp = f"{erp:.2f}%"
marketCap = "{:.1f} M€".format(marketCap / 1e6)
Current_Share_Price = f"{Current_Share_Price:.2f}€"
shares_outstanding = "{:.1f} M".format(shares_outstanding / 1e6)
definitive_coef_0 = f"{definitive_coef_0:.2f}"
definitive_coef_1 = f"{definitive_coef_1:.2f}"
definitive_coef_2 = f"{definitive_coef_2:.2f}"
cost_of_equity = cost_of_equity * 100
cost_of_equity = f"{cost_of_equity:.2f}%"


import streamlit as st
import pandas as pd

st.subheader('The Equity Risk Premium')

st.metric("The risk free rate of Belgium", erp)

st.subheader('Market capitalization')
col1, col2, col3 = st.columns(3)
col1.metric("Shares outstanding", shares_outstanding)
col2.metric("Current Share Price" ,Current_Share_Price)
col3.metric("Market capitalization" ,marketCap)



st.subheader('Cost of Equity')

import streamlit as st
import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

col1, col2, col3,col4 = st.columns(4)
col1.metric("beta for the market risk", definitive_coef_0)
col2.metric("beta for high-risk company" ,definitive_coef_2)
col3.metric("beta for low-risk company" ,definitive_coef_1)
col4.metric("Cost of Equity",cost_of_equity )

 # colour only metric text
ColourWidgetText(cost_of_equity, '#0a7ed1')       # colour metric value



import streamlit as st

st.title("DCF")
import sys
sys.path.append('/Users/gavysingh/Downloads/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path

from Valuation import sum_DCF,Discounted_Terminal_Value,Forecasted_Enterprise_Value,mv_debt,last_cash,Forecasted_Market_Cap,Forecasted_Share_Price,Current_Share_Price,gap_in_pct,wacc,share_price_mt
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


sum_DCF = "{:.1f} M".format(sum_DCF)
Discounted_Terminal_Value = "{:.1f} M".format(Discounted_Terminal_Value)
Forecasted_Enterprise_Value = "{:.1f} M".format(Forecasted_Enterprise_Value)
last_cash = "{:.1f} M".format(last_cash)
mv_debt = "{:.1f} M".format(mv_debt/1e6)
wacc = wacc * 100
wacc = f"{wacc:.2f}%"
Current_Share_Price1 = f"{Current_Share_Price:.2f}€"
Forecasted_Share_Price1 = f"{Forecasted_Share_Price:.2f}€"
gap_in_pct = f"{gap_in_pct:.2f}%"

import streamlit as st
import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    
    
    components.html(f"{htmlstr}", height=0, width=0)
    
    
col1, col2, col3,col4 = st.columns(4)
col1.metric("WACC", wacc)
col2.metric("Dicounted Cash Flows", sum_DCF)
col3.metric("Discounted Terminal Value" ,Discounted_Terminal_Value)
col4.metric("Forecasted Enterprise Value" ,Forecasted_Enterprise_Value)
col1.metric("Market Value of Debt",mv_debt )
col2.metric("Cash & Short Term Equivalents",last_cash )
col3.metric("Current Share Price",Current_Share_Price1 )
col4.metric("Forecasted Share Price",Forecasted_Share_Price1, gap_in_pct )


 # colour only metric text       # colour metric value
ColourWidgetText('Forecasted Share Price', '#0a7ed1')  # colour only metric text
ColourWidgetText(Forecasted_Share_Price1, '#0a7ed1') 

import streamlit as st
import plotly.graph_objects as go

# First graph
fig1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=Forecasted_Share_Price,
    title={'text': "Price"},
    domain={'x': [0, 1], 'y': [0, 1]}
))

# Second graph
fig2 = go.Figure()
fig2.add_trace(go.Indicator(
    mode="delta",
    value=Forecasted_Share_Price,
    delta={'reference': Current_Share_Price},
    domain={'row': 1, 'column': 1}
))

# Set the size of the figures
fig1.update_layout(width=300, height=400)
fig2.update_layout(width=400, height=400)

# Create a layout with two columns
col1, col2 = st.columns(2)

# Display the first graph in the first column
with col1:
    st.plotly_chart(fig1)

# Display the second graph in the second column
with col2:
    st.plotly_chart(fig2)
    
st.subheader('Monte Carlo Simulation')    


import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Assuming you have the data in a variable called share_price_mt
fig = px.histogram(share_price_mt, nbins=50)
fig.update_layout(
    xaxis_title="Share prices",
    yaxis_title="Frequency",
)

# Adding a vertical line for the current share price
current_share_price = Current_Share_Price
fig.add_vline(x=current_share_price, line_color='red', line_dash='dash', line_width=1,
              name='Current Share Price', annotation_text='Current Share Price')
fig.update_layout(
    legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="right", x=0.99),
)

st.plotly_chart(fig)





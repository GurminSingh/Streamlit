import streamlit as st

st.title("WACC")
import sys
sys.path.append('https://github.com/GurminSingh/Streamlit.git')  # Replace 'path/to/directory' with the actual path

from Valuation import cost_of_equity,cost_of_debt,cap_structure,w_cost_equity,w_cost_debt,wacc
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

cost_of_equity = cost_of_equity * 100
cost_of_equity = f"{cost_of_equity:.2f}%"
cost_of_debt = cost_of_debt * 100
cost_of_debt = f"{cost_of_debt:.2f}%"
w_cost_equity = w_cost_equity * 100
w_cost_equity = f"{w_cost_equity:.2f}%"
w_cost_debt = w_cost_debt * 100
w_cost_debt = f"{w_cost_debt:.2f}%"
wacc = wacc * 100
wacc = f"{wacc:.2f}%"
cap_structure = "{:.1f} M".format(cap_structure / 1e6)



import streamlit as st
import streamlit.components.v1 as components

def ColourWidgetText(wgt_txt, wch_colour = '#000000'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
                        elements[i].style.color = ' """ + wch_colour + """ '; } </script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

col1, col2, col3,col4,col5 = st.columns(5)
col1.metric("Cost of equity", cost_of_equity)
col2.metric("Cost of debt" ,cost_of_debt)
col3.metric("Capital structure" ,cap_structure)
col4.metric("Weight of cost equity",w_cost_equity )
col5.metric("Weight of cost debt",w_cost_debt )
col3.metric("WACC",wacc )

 # colour only metric text
ColourWidgetText(wacc, '#0a7ed1')       # colour metric value











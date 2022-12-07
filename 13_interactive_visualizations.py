'''
Interactive Visualizations (Plotly, Bokeh, Altair)

st.line_chart()
st.area_chart()
st.bar_chart()

st.plotly_chart()
st.bokeh_chart()
st.altair_chart()

'''

import pandas as pd
import numpy as np
import streamlit as st

## BASIC CHARTS

sample = pd.DataFrame(np.random.randint(low=10, high=20, size=(5,3)), columns=["A", "B", "C"])

st.subheader("Basic Streamlit Charts")

st.bar_chart(sample)
st.area_chart(sample)
st.line_chart(sample)

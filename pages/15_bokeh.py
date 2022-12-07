'''
Bokeh
'''
import pandas as pd
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import streamlit as st

st.subheader("Bokeh Line Chart")

x = [1,2,3,4,5]
y = [6,7,2,4,5]

p = figure(title="Simple Line Chart", 
            x_axis_label = 'x', 
            y_axis_label="y",)
p.line(x,y, line_width=2)
p.circle(x,y, size=10)
st.bokeh_chart(p)

# 1. Scatter plot between total_bill and tip
# 2. Scatter plot between total_bill and tip color by options (sex, smoker, day, time)

data = pd.read_csv('tips.csv')
st.subheader('1. Scatter plot between total_bill and tip')

p = figure(title="Scatterplot between total_bill and tips")
p.circle('total_bill', 'tip', source=data, size=12)
st.bokeh_chart(p)

st.markdown('---')
st.subheader('2. Scatter plot between total_bill and tip color by options (sex, smoker, day, time)')

select = st.selectbox("Select the categories: ", ('sex', 'smoker', 'day', 'time'))
color_palette = ['blue', 'green', 'red', 'yellow']
unique_cats = data[select].unique()
index_cmap = factor_cmap(select, palette=color_palette[:len(unique_cats)], factors = sorted(unique_cats))


p = figure(title="Scatter Plot and coloring by categories")
p.circle('total_bill', 'tip', source=data, fill_color=index_cmap, size=12, legend=select)
st.bokeh_chart(p)


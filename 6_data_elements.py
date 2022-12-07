'''
Displaying Dataframes
'''
import streamlit as st
import pandas as pd

st.header("st.dataframe")
st.caption("Display a dataframe as an interactive table")

df = pd.read_csv('tips.csv')
st.header("st.dataframe")
st.dataframe(df)

st.header("st.write")
st.write(df)

st.header("st.table")
st.table(df.head(5))

st.header("st.json")
st.json(df.head(3).to_dict())

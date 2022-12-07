'''
APIs
'''
import streamlit as st
import pandas as pd
import numpy as np

#display almost anything
# st.write()
st.write("Hello World")
st.write("Welcome to Streamlit App APIs")
st.write(1,2,3,4,5)

df = pd.DataFrame({
    "First Column": [1,2,3,4],
    "Second Column": [10,20,30,40]
})
st.write(df)

##display numpy array
st.write(np.array([1,2,3,4]))

## -------------------------- MAGIC ---------
st.write("Magic Commands")

df1 = pd.DataFrame({
    "col1": [1,2,3,4]
})
df1

x=10
x

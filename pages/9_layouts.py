'''
Layouts
'''
import streamlit as st
import pandas as pd
import time

side_bar = st.sidebar
side_bar.header("Sidebar's Header")
side_bar.caption("Elements that get added in the sidebar are pinned to the left")

st.title("Display a custom dataframe")

#load tips 
df = pd.read_csv('tips.csv')

columns = tuple(df.columns)
st.write(columns)

#create widget select box
select_column = side_bar.selectbox("Select the column that you want to display", columns)

side_bar.write(f"You selected the column_name = {select_column}")

#Display the dataframe
st.dataframe(df[[select_column]])


#Columns
st.header("Columns - st.columns()")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column1")
    st.image("image.jpg", width=200)

with col2:
    st.subheader("Column2")
    st.dataframe(df)

with col3:
    st.subheader("Column3")
    st.dataframe(df)

# Expander

st.subheader("Expander - st.expander()" )

with st.expander("Some Explanation"):
    st.write('''
    Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. 
Donec sollicitudin molestie malesuada. Donec sollicitudin molestie malesuada. Vivamus 
suscipit tortor eget felis porttitor volutpat. Proin eget tortor risus. Nulla quis 
lorem ut libero malesuada feugiat. Quisque velit nisi, pretium ut lacinia in, elementum 
id enim. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem.
    ''')


#Containers

st.header("Containers")
with st.container():
    st.write("You are inside a container")

# Empty Layout
# Only holds a single element at a single point of time and after that it gets removed

st.header("Empty - st.empty()")

placeholder = st.empty()

for i in range(1,11):
    placeholder.write(f"This message will dissapear in {10-i} seconds")
    time.sleep(1)

placeholder.empty()

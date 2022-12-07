'''
Registration Form
'''
import datetime
import streamlit as st

st.title("Registration Form")

#3 columns
col1, col2, col3 = st.columns(3)

with col1:
    title = st.selectbox("", ("Mr", "Mrs", "Miss"))

with col2:
    name = st.text_input("Name")

with col3:
    lastname = st.text_input("Last Name")

designation = st.selectbox("Designation", ("Software", "Sr. Software", "Technical Lead", "Manager", "Sr. Manager", "Project Manager"))

dob = st.date_input("Date of Birth", min_value=datetime.date(1910, 1, 1))

gender = st.radio("Select Gender", ("Male", "Female"))

age = st.slider("Age", min_value=0, max_value=110, step=1, value=20)

dict1 = {
    "Title": title,
    "First Name": name,
    "Last Name": lastname,
    "Designation": designation,
    "Date of Birth": dob,
    "Gender": gender,
    "Age": age
}

submit = st.button("Submit")
if submit:
    st.json(dict1)
    st.success("Data Submitted successfully")

'''
Status Elements
'''
import time
import streamlit as st

st.header("Status Bar - st.progress()")
mybar = st.progress(0)
def progress_bar():
    ''' progress bar '''
    for percent_complete in range(1,101):
        time.sleep(0.1)
        mybar.progress(percent_complete)


st.header("Spinner - st.spinner()")
with st.spinner("Something is processing ..."):
    progress_bar()

st.header("Status Messages")

st.subheader("Info Message")
st.info("This is information Message")
st.success("This is a success message")
st.error("This is an error message")

st.subheader("Balloons")
time.sleep(0.5)
st.balloons()


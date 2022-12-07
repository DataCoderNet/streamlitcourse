'''
Media files
'''
import streamlit as st

st.header("Display an Image - st.image()")
st.image("image.jpg", caption="Beautiful city", width=500)

st.header("Display a video")
video_file = open('waterfalls.mp4', "rb")
video_bytes = video_file.read()
st.video(video_bytes, format="mp4")

st.header("Audio Files")
audio_files = open('audio.mp3', "rb")
audio_bytes = audio_files.read()
st.audio(audio_files, format="audio/ogg")

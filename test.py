import streamlit as st
st.title("Testing connection")



st.image("./img1.jpg")
st.write("display video")
video_file = open('Creative202.mp4', 'rb') #enter the filename with filepath

video_bytes = video_file.read() #reading the file

st.video(video_bytes) #displaying the video






import mysql.connector

import streamlit as st
import yt_dlp
import os

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक डालें:")

if st.button("डाउनलोड और प्रोसेस करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है...")
        ydl_opts = {'format': 'best', 'outtmpl': 'downloaded_video.mp4'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.success("वीडियो डाउनलोड हो गया! अब क्लिप्स बन रहे हैं...")
        # यहाँ क्लिप्स बनाने (MoviePy) वाला कोड आगे जोड़ेंगे
    else:
        st.error("कृपया पहले लिंक डालें!")

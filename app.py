import streamlit as st
import yt_dlp
import os

st.title("वायरल क्लिप्स मेकर")
import streamlit as st
import yt_dlp

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक डालें:")

if st.button("डाउनलोड और प्रोसेस करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है...")
        # नई बेहतर सेटिंग्स
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': 'downloaded_video.mp4',
            'noplaylist': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("वीडियो डाउनलोड हो गया! अब क्लिप्स बन रहे हैं...")
        except Exception as e:
            st.error(f"डाउनलोडिंग में समस्या आई: {e}")
    else:
        st.error("कृपया पहले लिंक डालें!")

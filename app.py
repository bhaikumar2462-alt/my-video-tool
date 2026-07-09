import streamlit as st
import yt_dlp

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("डाउनलोड करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है, कृपया प्रतीक्षा करें...")
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',
            'noplaylist': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("वीडियो सफलतापूर्वक डाउनलोड हो गया!")
            st.video("downloaded_video.mp4")
        except Exception…

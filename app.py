import streamlit as st
import yt_dlp

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("डाउनलोड करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है...")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',
            'noplaylist': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("वीडियो डाउनलोड हो गया!")
            st.video("downloaded_video.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया लिंक डालें")import streamlit as st
import yt_dlp

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("डाउनलोड करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है...")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',
            'noplaylist': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("वीडियो डाउनलोड हो गया!")
            st.video("downloaded_video.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("कृपया लिंक डालें")   

import streamlit as st
import yt_dlp

st.title("वायरल क्लिप्स मेकर")
url = st.text_input("वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("डाउनलोड करें"):
    if url:
        st.write("डाउनलोडिंग शुरू हो रही है, कृपया प्रतीक्षा करें...")
        
        # 'best' सेटिंग का उपयोग किया है ताकि ffmpeg की ज़रूरत न पड़े
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',
            'noplaylist': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("वीडियो सफलतापूर्वक डाउनलोड हो गया!")
            st.video("downloaded_video.mp4")
        except Exception as e:
            st.error(f"डाउनलोडिंग में समस्या आई: {e}")
    else:
        st.warning("कृपया पहले एक वैध लिंक डालें।")

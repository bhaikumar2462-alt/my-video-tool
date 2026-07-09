import streamlit as st
import yt_dlp
from moviepy.editor import VideoFileClip
import os

st.title("वायरल क्लिप मेकर")

url = st.text_input("यूट्यूब वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("क्लिप बनाएं"):
    if url:
        try:
            # पुरानी फाइलें हटाएं (अगर कोई बची हों)
            if os.path.exists("downloaded_video.mp4"): os.remove("downloaded_video.mp4")
            if os.path.exists("viral_clip.mp4"): os.remove("viral_clip.mp4")

            st.write("डाउनलोडिंग शुरू हो रही है...")
            
            # सिर्फ mp4 फॉर्मेट डाउनलोड करें (ffmpeg की जरूरत नहीं पड़ेगी)
            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': 'downloaded_video.mp4',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            st.write("डाउनलोड पूरा हुआ! अब क्लिप काट रहे हैं...")
            
            # 0 से 30 सेकंड का क्लिप बनाना
            video = VideoFileClip("downloaded_video.mp4")
            clip = video.subclip(0, 30)
            clip.write_videofile("viral_clip.mp4", codec="libx264", audio_codec="aac")
            
            st.video("viral_clip.mp4")
            st.success("आपकी क्लिप तैयार है!")
            
        except Exception as e:
            st.error(f"एरर आया: {e}")

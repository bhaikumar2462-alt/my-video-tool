import streamlit as st
import yt_dlp
from moviepy.editor import VideoFileClip
import os

st.title("वायरल क्लिप मेकर")

url = st.text_input("यूट्यूब वीडियो का लिंक यहाँ पेस्ट करें:")

if st.button("क्लिप बनाएं"):
    if url:
        try:
            st.write("डाउनलोडिंग शुरू हो रही है...")
            
            # yt-dlp ऑप्शंस
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'downloaded_video.mp4',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            st.write("वीडियो डाउनलोड हो गया! अब क्लिप काट रहे हैं...")
            
            # MoviePy से क्लिप काटना
            video = VideoFileClip("downloaded_video.mp4")
            clip = video.subclip(0, 30) # 0 से 30 सेकंड का क्लिप
            clip.write_videofile("viral_clip.mp4", codec="libx264")
            
            st.video("viral_clip.mp4")
            st.success("आपकी क्लिप तैयार है!")
            
        except Exception as e:
            st.error(f"Error: {e}")

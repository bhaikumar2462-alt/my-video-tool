from moviepy.editor import VideoFileClip
import streamlit as st
import yt_dlp

def make_clips(video_path):
    video = VideoFileClip(video_path)
    # 0 से 30 सेकंड का क्लिप बनाना
    clip = video.subclip(0, 30) 
    clip.write_videofile("clip1.mp4")
    return "clip1.mp4"

# Streamlit UI में बटन दबाने पर क्लिप बनाने का फंक्शन कॉल करें

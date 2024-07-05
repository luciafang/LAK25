import moviepy.editor as mp
import speech_recognition as sr
import time

# Load the video
video = mp.VideoFileClip("/Users/lucia/Downloads/lucia.MOV")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("lucia.wav", nbytes=4)
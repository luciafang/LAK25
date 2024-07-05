# import speech_recognition as sr
#
#
# # Initialize recognizer
# r = sr.Recognizer()
#
# # Load the audio file
# with sr.AudioFile("audio_clip_5.wav") as source:
#     # r.energy_threshold = 10
#     # r.dynamic_energy_threshold = False
#     r.adjust_for_ambient_noise(source)
#     audio = r.record(source)
#     text = r.recognize_google(audio)
# # Function to recognize speech with retries
#
# # Print the text
# print("\nThe resultant text from video is: \n")
# print(text)
import os

from openai import OpenAI

# os.chdir('../')
# print(os.getcwd())
# print(os.environ.get('OPENAI_API_KEY'))
client = OpenAI(api_key='sk-proj-AY1xM1B9DtahgLJm6PoxT3BlbkFJSdVtgdPgQ37SNrDj6eJY')

# audio_file = open("audio_clip_5.wav", 'rb')
# transcription = client.audio.transcriptions.create(model='whisper-1', file=audio_file)
# print(transcription.text)
# Function to transcribe audio using OpenAI's transcription service
def transcribe_audio(client, file_path):
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="srt"
        )
        # Pass the transcription directly for processing
        return process_transcription(transcription)
        #return response  # Directly return the response, assuming it's the transcription text

# Function to process the raw transcription into the desired format
def process_transcription(transcription):
    blocks = transcription.split('\n\n')
    processed_lines = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            time_range = lines[1]
            text = lines[2]
            start_time = time_range.split(' --> ')[0]
            # Convert the time format from "00:00:00,000" to "0:00:00"
            formatted_start_time = start_time
            processed_line = f"[{formatted_start_time}]{text}"
            processed_lines.append(processed_line)
    return '\n'.join(processed_lines)


transcription = transcribe_audio(client, 'audio_clip_5.wav')
f = open("audio_clip_5.txt", "a")
f.write(transcription)
f.close()
# print(transcription)

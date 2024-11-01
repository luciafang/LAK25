import pandas as pd
import openai


# all transcripts to chatgpt
openai.api_key = "sk-proj-AY1xM1B9DtahgLJm6PoxT3BlbkFJSdVtgdPgQ37SNrDj6eJY"


def split_confused_transcripts(transcript_with_confused_df):
    confused_transcripts_df = transcript_with_confused_df[transcript_with_confused_df.state=='Confused']
    # confused_transcript = ' '.join(confused_transcripts_df.transcript.to_list())
    # all_transcripts = ' '.join(transcript_with_confused_df.transcript.to_list())
    all_transcripts = ''
    for line in transcript_with_confused_df.transcript.to_list():
        all_transcripts += str(line)

    confused_transcript = ''
    for line in confused_transcripts_df.transcript.to_list():
        confused_transcript += str(line)

    return confused_transcript, all_transcripts

def split_confused_transcripts_by_line(transcript_with_confused_df):
    confused_transcripts_df = transcript_with_confused_df[transcript_with_confused_df.state=='Confused']
    # confused_transcript = ' '.join(confused_transcripts_df.transcript.to_list())
    # all_transcripts = ' '.join(transcript_with_confused_df.transcript.to_list())
    all_transcripts = ''
    for line in transcript_with_confused_df.transcript.to_list():
        all_transcripts += (str(line)+'\n')

    confused_transcript = ''
    for line in confused_transcripts_df.transcript.to_list():
        confused_transcript += (str(line)+'\n')

    return confused_transcript, all_transcripts



# send to chatgpt
def send2chatgpt(all_transcripts, confused_transcripts):
    messages = [{"role": "system", "content": "You are a college professor"}]
    messages.append({"role": "user",
                     "content": f"Based on lecture transcript: {all_transcripts}, "
                                f"where I am confused on the following lecture transcripts: {confused_transcripts}."
                                f"Identify the theme and course topic where I most likely was confused."
                                f"Use the theme to provide me a concise and informative topic summary."
                                f"Limit the response to just the summary (5 sentences max),"
                                f"Make it into a concept then with explanation. Make it organized."})
    answers = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    return answers.choices[0].message.content


# confused part to display text
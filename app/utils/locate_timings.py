import pandas as pd
from glob import glob
import numpy as np
import streamlit as st

# find the confusion time point
# bin to a min, each is 2 sec
def bin_confusion(confusion_csv, bin_size=30, source_duration=2400):
    df = pd.read_csv(confusion_csv, index_col=0)

    df.fillna(value='none', inplace=True)
    emotions_list = ['Not Confused', 'Confused']

    all_emotion_ratios = []
    for row in range(df.shape[0]):
        # emotion_ratios = {key:0 for key in emotions_list}
        # confusion_vals = []
        emotion, counts = np.unique(df.iloc[row, 1:].values, return_counts=True)
        idx_none = emotion == 'none'
        emotion_not_none = emotion[~idx_none]
        # ratio = counts[~idx_none]
        ratio = counts[~idx_none] / np.sum(counts[~idx_none])
        # for emo, rats in zip(emotion_not_none, ratio):
        #     emotion_ratios[emo] = rats
        for emo, rats in zip(emotion_not_none, ratio):
            if emo == 'Confused':
                confusion_vals = rats
        # all_emotion_ratios.append(emotion_ratios)
        all_emotion_ratios.append(confusion_vals)


    avg_1min = []
    for i in range(0, source_duration, bin_size):
        avg_1min.append(np.mean(all_emotion_ratios[i:i + bin_size]))


    return avg_1min

def bin_confusion_from_df(df, bin_size=30, source_duration=2400):

    df.fillna(value='none', inplace=True)
    emotions_list = ['Not Confused', 'Confused']

    all_emotion_ratios = []
    for row in range(df.shape[0]):
        # emotion_ratios = {key:0 for key in emotions_list}
        # confusion_vals = []
        emotion, counts = np.unique(df.iloc[row, 1:].values, return_counts=True)
        idx_none = emotion == 'none'
        emotion_not_none = emotion[~idx_none]
        # ratio = counts[~idx_none]
        ratio = counts[~idx_none] / np.sum(counts[~idx_none])
        # for emo, rats in zip(emotion_not_none, ratio):
        #     emotion_ratios[emo] = rats
        for emo, rats in zip(emotion_not_none, ratio):
            if emo == 'Confused':
                confusion_vals = rats
        # all_emotion_ratios.append(emotion_ratios)
        all_emotion_ratios.append(confusion_vals)


    avg_1min = []
    for i in range(0, source_duration, bin_size):
        avg_1min.append(np.mean(all_emotion_ratios[i:i + bin_size]))


    return avg_1min

# go to transcript, find the locate timestamp
def confusion2transcript(trancript_csv, avg_1min):
    # a= np.mean(avg_1min)
    # b = np.std(avg_1min)
    # c = a+b
    # top_confusion_min = np.array(np.where(avg_1min > c)[0])

    a = np.min(avg_1min)
    avg_1min_above_min = avg_1min / a
    c = 2
    top_confusion_min = np.array(np.where(avg_1min_above_min > c)[0])

    df = pd.read_csv(trancript_csv)
    df['state']='Not Confused'
    print(top_confusion_min)
    for min in top_confusion_min:
        print(min)
        prev_min = min-1
        prev_min_zfill = str(prev_min).zfill(2)
        print(prev_min_zfill)
        min_zfill = str(min).zfill(2)
        print(min_zfill)

        df.state[(df.timestamp < normalize_time(f"00:{min_zfill}:00")) &
                 (df.timestamp >= normalize_time(f"00:{prev_min_zfill}:00"))] = 'Confused'
    return df


# def normalize_time(time_str):
#     # Split the time string into hours, minutes, and seconds
#     hours, minutes, seconds = map(int, time_str.split(':'))
#
#     # Calculate the total minutes and then the new hours and minutes
#     total_minutes = minutes
#     new_hours = hours + total_minutes // 60
#     new_minutes = total_minutes % 60
#
#     # Format the new time string
#     normalized_time_str = f"{new_hours:02}:{new_minutes:02}:{seconds:02}"
#
#     return normalized_time_str


def normalize_time(time_str):
    # Split the time string into hours, minutes, and seconds
    hours, minutes, seconds = map(float, time_str.split(':'))

    # Calculate the total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(total_seconds)
    # Calculate the new hours, minutes, and seconds
    new_hours = total_seconds // 3600
    total_seconds %= 3600
    new_minutes = total_seconds // 60
    new_seconds = total_seconds % 60

    # Format the new time string
    normalized_time_str = f"{int(new_hours):02}:{int(new_minutes):02}:{int(new_seconds):02}"
    print(normalized_time_str)
    return normalized_time_str
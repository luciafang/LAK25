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
        ratio = counts[~idx_none]
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
    a= np.mean(avg_1min)
    b = np.std(avg_1min)
    c = a+b
    confusion_top5_percent_min = np.array(np.where(avg_1min > c)[0])

    df = pd.read_csv(trancript_csv)
    df['state']='Not Confused'
    for min in confusion_top5_percent_min:
        df.state[(df.timestamp < f"00:{min}:00")
                  & (df.timestamp >= f"00:{min-1}:00")] = 'Confused'
    return df


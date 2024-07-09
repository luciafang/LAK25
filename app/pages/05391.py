import streamlit as st
import datetime
from glob import glob
from utils.locate_timings import bin_confusion, confusion2transcript
from utils.identify_theme import send2chatgpt, split_confused_transcripts
from PIL import Image
import numpy as np
import base64
import io


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(
    page_title='UnderstandMe',
    page_icon='logo_icon.png',
    layout="wide",
    menu_items={
        'Report a bug': 'https://www.linkedin.com/feed/'
    })

page_banner_img = """
<style>
[data-testid="stHeader"] {
background-color: #2085B7;
opacity: 1;
background: repeating-linear-gradient( 45deg, #2085B7, #2085B7 2px, #2085B7 2px, #2085B7 10px );
}
</style>
"""
st.markdown(page_banner_img, unsafe_allow_html=True)


local_css("style.css")

file = open("./logo.png", "rb")
contents = file.read()
img_str = base64.b64encode(contents).decode("utf-8")
buffer = io.BytesIO()
file.close()
img_data = base64.b64decode(img_str)
img = Image.open(io.BytesIO(img_data))
resized_img = img.resize((250, 250))  # x, y
resized_img.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url('data:image/png;base64,{img_b64}');
                background-repeat: no-repeat;
                padding-top: 200px;
                background-position: 50px -38px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


all_csv = glob('../confusion_processed/*')
all_dates = []
for csv in all_csv:
    date = datetime.datetime.strptime(csv.split('/')[-1].replace('_confusion', '').split('.')[0],
                                      '%Y%m%d')
    # st.write(date)
    all_dates.append(date)

st.markdown(f" <h1 style='text-align: center; font-size:40px; "
                f"font-family:sans-serif; font-weight:normal'>"
                f"Choose a date to view the most <span style = 'color:#2085B7'>confused</span> concepts!</h3> "
                , unsafe_allow_html=True)

d = st.date_input('Select a session date:', datetime.date(2019, 1, 31))
d = datetime.datetime.strptime(str(d).replace('-', ''), "%Y%m%d")


if d not in all_dates:
    st.error('There is no session on this date. Please select a correct session date')
else:

    select_confused_csv = '../confusion_processed/'+str(d.year)+str(d.month).zfill(2)+str(d.day).zfill(2)+'_confusion.csv'
    percent_confusion = bin_confusion(select_confused_csv)
    # st.write(percent_confusion)
    select_transcript_csv = '../transcripts_processed/' + str(d.year) + str(d.month).zfill(2) + str(d.day).zfill(
        2) + '_transcript_all.csv'
    transcript_with_confused_df = confusion2transcript(select_transcript_csv, percent_confusion)
    confused_transcript, all_transcripts = split_confused_transcripts(transcript_with_confused_df)
    response = send2chatgpt(all_transcripts, confused_transcript)

    image = Image.open('harrison.jpeg')

    with st.chat_message('user', avatar = np.array(image)):
        st.write(response)
    # df = pd.read_csv(select_csv, index_col=0)
    # st.dataframe(df)
# a function that takes the confusion csv, bin two second into a min
# find the values are greater than threshold 40%

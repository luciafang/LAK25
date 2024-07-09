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
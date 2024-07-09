import streamlit as st
import io
from PIL import Image
import base64


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


# st.header('Welcome :blue[Lucia]!', divider = 'rainbow')
st.markdown("", unsafe_allow_html=True)
# st.markdown(f" <h1 style='text-align: left; color: #2085B7; font-size:20px; "
#                 f"font-family:Avenir; font-weight:normal'>"
#                 f"Lucia</h1> "
#                 , unsafe_allow_html=True)
st.markdown(f" <h1 style='text-align: left; font-size:40px; "
                f"font-family:sans-serif; font-weight:normal'>"
                f"Welcome <span style = 'color:#2085B7'>Lucia</span>!</h1> "
                , unsafe_allow_html=True)
# st.divider()
# st.markdown("div[data=testid='stExpander' div[role='button'] p {font-size:2rem;}", unsafe_allow_html=True)

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



col1, col2= st.columns(2)
with col1:
    # st.subheader('05391 - Designing Human-Centered Software')

    with st.expander('05391 - Designing Human-Centered Software', expanded=True):
        st.write("Why are things so hard to use these days? "
                    "Why doesn't this thing I just bought work? "
                    "Why is this web site so hard to use? These are "
                    "frustrations that we have all faced from systems "
                    "not designed with people in mind. The question "
                    "this course will focus on is: how can we design "
                    "human-centered systems that people find useful "
                    "and usable? This course is a broad introduction "
                    "to designing, prototyping, and evaluating user "
                    "interfaces. If you take only one course in Human-Computer "
                    "Interaction, this is the course for you. We will cover "
                    "theory as well as practical application of ideas from "
                    "Human-Computer Interaction. Coursework includes lectures, "
                    "class discussion, homework, class presentations, and group "
                    "projects. This class is open to all undergrads and grad "
                    "students, with either technical or non-technical majors. "
                    "However, there is a programming prerequisite.")
    # st.text_area("",
    #                 "Why are things so hard to use these days? "
    #                 "Why doesn't this thing I just bought work? "
    #                 "Why is this web site so hard to use? These are "
    #                 "frustrations that we have all faced from systems "
    #                 "not designed with people in mind. The question "
    #                 "this course will focus on is: how can we design "
    #                 "human-centered systems that people find useful "
    #                 "and usable? This course is a broad introduction "
    #                 "to designing, prototyping, and evaluating user "
    #                 "interfaces. If you take only one course in Human-Computer "
    #                 "Interaction, this is the course for you. We will cover "
    #                 "theory as well as practical application of ideas from "
    #                 "Human-Computer Interaction. Coursework includes lectures, "
    #                 "class discussion, homework, class presentations, and group "
    #                 "projects. This class is open to all undergrads and grad "
    #                 "students, with either technical or non-technical majors. "
    #                 "However, there is a programming prerequisite.",
    #              height = 500, label_visibility='collapsed')

with col2:
    with st.expander('67272 - Placeholder Course', expanded=True):
        st.write("Placeholder for description. Here is another course description.")
    # st.subheader('Course2')

    # st.text_area("", "Course2 Description Example", label_visibility='collapsed')


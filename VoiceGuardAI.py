import base64
import streamlit as st

st.set_page_config(
    page_title="VoiceGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)
def set_background(image_file):

    with open(image_file, "rb") as img:

        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{

            background:
                linear-gradient(
                    rgba(6,12,24,0.82),
                    rgba(6,12,24,0.82)
                ),
                url("data:image/png;base64,{encoded}");

            background-size: cover;

            background-position: center;

            
            background-repeat: no-repeat;

            background-attachment: fixed;

        }}

        </style>
        """,
        unsafe_allow_html=True
    )
set_background("assets/wallpaper.png")
with open("assets/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

st.switch_page("pages/Home.py")

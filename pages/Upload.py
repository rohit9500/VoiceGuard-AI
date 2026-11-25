
import streamlit as st
import os

# Load CSS
with open("assets/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )
from utils.ui import set_background

set_background()
from utils.header import header

header()

st.markdown("""
<div class="hero-card">

<div class="hero-title">

📂 Upload Audio or Video

</div>

<div class="hero-sub">

Upload any audio or video file and let VoiceGuard AI detect

✔ Deepfake Voices

✔ Scam Conversations

✔ Risk Score

✔ Generate PDF Report

</div>

</div>
""",unsafe_allow_html=True)
st.markdown(
"""
Upload an **audio** or **video** file to begin AI-powered analysis.

VoiceGuard AI supports Deepfake Voice Detection, Speech-to-Text,
Scam Detection and Professional PDF Report Generation.
"""
)

st.divider()

uploaded_file = st.file_uploader(
    "",
    type=[
        "wav",
        "mp3",
        "mp4",
        "avi",
        "mov",
        "mkv"
    ],
    help="Supported Formats : WAV, MP3, MP4, AVI, MOV, MKV"
)
st.write("### Supported Formats")

c1,c2=st.columns(2)

with c1:

    st.success("🎵 WAV")

    st.success("🎵 MP3")

with c2:

    st.success("🎥 MP4")

    st.success("🎥 AVI")

    st.success("🎥 MOV")

    st.success("🎥 MKV")

st.markdown("</div>",unsafe_allow_html=True)

if uploaded_file:

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    left, right = st.columns([2,1])

    with left:

        st.subheader("🎥 Preview")

        if extension in [".mp4", ".avi", ".mov", ".mkv"]:

            st.video(uploaded_file)

        else:

            st.audio(uploaded_file)

    with right:

        st.subheader("📄 File Information")

        st.metric(
            "Filename",
            uploaded_file.name
        )

        st.metric(
            "File Size",
            f"{uploaded_file.size/1024/1024:.2f} MB"
        )

        st.metric(
            "Format",
            extension.replace(".","").upper()
        )

        if extension in [".wav",".mp3"]:

            st.success("🎵 Audio File")

        else:

            st.success("🎬 Video File")

    st.divider()

    st.markdown(
'<div class="section-title">🤖 AI Modules</div>',
unsafe_allow_html=True
)
    st.divider()

    st.markdown("## 🚀 Ready to Analyze?")

    if st.button(
        "🔍 Initialize AI Analysis",
        use_container_width=True,
        type="primary"
    ):
        st.session_state["audio"] = uploaded_file

        st.switch_page("pages/Deepfake.py")

a,b,c,d=st.columns(4)

with a:

    st.markdown("""

<div class="feature-card">

<h2>🎤</h2>

<b>Deepfake Voice Detection</b>

</div>

""",unsafe_allow_html=True)

with b:

    st.markdown("""

<div class="feature-card">

<h2>📝</h2>

<b>Speech Whisper</b>


</div>

""",unsafe_allow_html=True)

with c:

    st.markdown("""

<div class="feature-card">

<h2> 🚨</h2>

<b>Scam Classification</b>

</div>

""",unsafe_allow_html=True)

with d:

    st.markdown("""

<div class="feature-card">

<h2> 📄 </h2>

<b>Report PDF Export</b>

</div>

""",unsafe_allow_html=True)
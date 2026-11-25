from utils.ui import set_background

set_background()
from utils.header import header

header()
import streamlit as st


def show_home():

    st.markdown("""

<div style="padding-top:25px;padding-bottom:20px;">

<h1 style="font-size:58px;
font-weight:800;
text-align:center;
margin-bottom:5px;
color:white;">

🛡 VoiceGuard AI

</h1>

<p style="text-align:center;
font-size:22px;
color:#9CA3AF;
margin-top:0px;">

AI Powered Deepfake Voice &
Scam Detection Platform

</p>

</div>

""",unsafe_allow_html=True)
left,right=st.columns([2,1])

with left:

    st.markdown("""
### Secure Every Voice Before You Trust It

VoiceGuard AI is an intelligent cybersecurity platform
that detects AI-generated voices, scam conversations
and fraudulent calls using Machine Learning and
Speech Intelligence.

✔ Deepfake Detection

✔ Scam Classification

✔ Speech Recognition

✔ Risk Analysis

✔ Professional PDF Reports

""")

    c1,c2=st.columns(2)

    with c1:

        if st.button(
            "🚀 Start Analysis",
             use_container_width=True):
             st.switch_page("pages/Upload.py")
    with c2:

       if st.button(
            "📄 View Reports",
            use_container_width=True
        ):
           st.switch_page("pages/History.py")

with right:

    st.image(
        "assets/logo.png",
        width=300
    )
st.divider()
st.markdown("## Live Statistics")

a,b,c,d=st.columns(4)

a.metric(
    "Detection Accuracy",
    "94.55%"
)

b.metric(
    "AI Models",
    "2"
)

c.metric(
    "Supported Formats",
    "6"
)

d.metric(
    "Reports Generated",
    "Unlimited"
)
st.divider()
##########################################################
# FEATURES
##########################################################

st.markdown(
    """
    <h2 style='text-align:center;
               color:#60A5FA;
               margin-bottom:30px;'>
               🚀 Core Features
    </h2>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div style="background:#172033;
padding:25px;
border-radius:18px;
border:1px solid #2F3E52;
margin-bottom:20px;">

<h3>🎤 Deepfake Voice Detection</h3>

Detect AI-generated voices using
Machine Learning and Audio Feature
Analysis.

✔ Random Forest

✔ MFCC Features

✔ Chroma Features

✔ Mel Spectrogram

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#172033;
padding:25px;
border-radius:18px;
border:1px solid #2F3E52;">

<h3>📝 Speech Recognition</h3>

Convert uploaded audio into text
using OpenAI Whisper.

✔ Fast

✔ Accurate

✔ Multi-language

</div>
""", unsafe_allow_html=True)


with col2:

    st.markdown("""
<div style="background:#172033;
padding:25px;
border-radius:18px;
border:1px solid #2F3E52;
margin-bottom:20px;">

<h3>🚨 Scam Detection</h3>

Analyze conversations for

✔ OTP Fraud

✔ Banking Scam

✔ Investment Scam

✔ Loan Scam

✔ Normal Conversation

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#172033;
padding:25px;
border-radius:18px;
border:1px solid #2F3E52;">

<h3>📄 Professional Reports</h3>

Generate complete PDF reports

✔ Deepfake Result

✔ Transcript

✔ Scam Analysis

✔ Risk Score

</div>
""", unsafe_allow_html=True)

st.divider()

##########################################################
# WORKFLOW
##########################################################

st.markdown(
    """
    <h2 style='text-align:center;
               color:#60A5FA;
               margin-bottom:30px;'>
               🔄 Detection Pipeline
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown("""

<div style="background:#172033;
padding:30px;
border-radius:18px;
border:1px solid #2F3E52;
text-align:center;
font-size:18px;
line-height:2.1;">

📂 Upload Audio / Video

⬇

🎵 Audio Extraction

⬇

🎤 Deepfake Detection

⬇

📝 Speech-to-Text

⬇

🚨 Scam Classification

⬇

⚠ Risk Analysis

⬇

📄 PDF Report

</div>

""", unsafe_allow_html=True)

st.divider()

##########################################################
# TECHNOLOGY
##########################################################

st.markdown(
    """
    <h2 style='text-align:center;
               color:#60A5FA;
               margin-bottom:30px;'>
               💻 Technology Stack
    </h2>
    """,
    unsafe_allow_html=True
)

a,b,c,d,e,f = st.columns(6)

a.success("🐍 Python")

b.success("🎯 Streamlit")

c.success("🧠 Whisper")

d.success("🌲 Random Forest")

e.success("📊 Plotly")

f.success("🗄 SQLite")

st.divider()
##########################################################
# WHY VOICEGUARD AI
##########################################################

st.markdown(
"""
<h2 style='text-align:center;
color:#60A5FA;
margin-bottom:25px;'>

🌍 Why VoiceGuard AI?

</h2>
""",
unsafe_allow_html=True
)

left,right=st.columns([3,2])

with left:

    st.markdown("""

VoiceGuard AI is an Artificial Intelligence powered
Cybersecurity platform developed to identify AI-generated
voices, scam conversations and fraudulent calls.

The system combines Machine Learning,
Speech Recognition and Audio Signal Processing
to provide accurate real-time analysis.

### Key Benefits

✔ Detect Deepfake Voices

✔ Detect Scam Conversations

✔ Generate Speech Transcript

✔ Analyze Audio Features

✔ Generate Professional PDF Reports

✔ Maintain Analysis History

""")

with right:

    st.info("""

### 🎯 Best Use Cases

🏦 Banking Fraud

📞 Fake Customer Support Calls

🎭 Voice Cloning

🎥 Deepfake Videos

👮 Digital Forensics

🏢 Enterprise Security

""")

st.divider()

##########################################################
# PROJECT HIGHLIGHTS
##########################################################

st.markdown(
"""
<h2 style='text-align:center;
color:#60A5FA;
margin-bottom:30px;'>

🏆 Project Highlights

</h2>
""",
unsafe_allow_html=True
)

a,b,c,d=st.columns(4)

a.metric("Libraries","15+")

b.metric("ML Models","2")

c.metric("Audio Features","40+")

d.metric("Supported Formats","6")

st.divider()

##########################################################
# FUTURE SCOPE
##########################################################

st.markdown(
"""
<h2 style='text-align:center;
color:#60A5FA;
margin-bottom:30px;'>

🚀 Future Enhancements

</h2>
""",
unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:

    st.success("""

✔ Live Call Detection

✔ Real-time Monitoring

✔ API Integration

""")

with col2:

    st.success("""

✔ Transformer Models

✔ Speaker Verification

✔ Multilingual Detection

""")

with col3:

    st.success("""

✔ Cloud Deployment

✔ Mobile Application

✔ Enterprise Dashboard

""")

st.divider()

##########################################################
# CALL TO ACTION
##########################################################

st.markdown(
"""
<div style="background:#172033;
padding:40px;
border-radius:18px;
border:1px solid #3B82F6;
text-align:center;">

<h2 style="color:white;">

Ready to Analyze?

</h2>

<p style="font-size:18px;
color:#CBD5E1;">

Upload your first Audio or Video
and let VoiceGuard AI detect
Deepfake Voices and Scam Conversations.

</p>

</div>
""",
unsafe_allow_html=True
)

if st.button(
    "🚀 Start Detection",
    use_container_width=True
):
    st.info("Open the Upload page from the navigation menu.")

st.divider()

##########################################################
# FOOTER
##########################################################

st.markdown(
"""
<div style="text-align:center;
padding:20px;">

<h4 style="color:#60A5FA;">

🛡 VoiceGuard AI

</h4>

<p style="color:#94A3B8;">

AI Powered Deepfake Voice & Scam Detection Platform

</p>

<p style="color:#64748B;font-size:14px;">

Built using Python • Streamlit • Whisper •
Random Forest • Librosa • Plotly • SQLite

</p>

</div>
""",
unsafe_allow_html=True
)
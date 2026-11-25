from utils.ui import set_background

set_background()
from utils.header import header

header()
import streamlit as st
import tempfile
import pandas as pd
import plotly.express as px
from utils.video_processor import VideoProcessor

from utils.audio_loader import AudioLoader
from utils.audio_statistics import AudioStatistics
from utils.audio_visualizer import AudioVisualizer

from utils.fake_detector import FakeVoiceDetector


st.title("🤖 Deepfake Voice Detection")

if "audio" not in st.session_state:

    st.warning("Upload audio first.")

    st.stop()

uploaded = st.session_state["audio"]
import os

extension = os.path.splitext(uploaded.name)[1]

with tempfile.NamedTemporaryFile(
    delete=False,
    suffix=extension
) as tmp:

    tmp.write(uploaded.getvalue())
    path = tmp.name


if VideoProcessor.is_video(uploaded.name):

    path = VideoProcessor.extract_audio(path)

loader = AudioLoader()

audio, sr = loader.load_audio(path)
detector = FakeVoiceDetector()
result = detector.predict(path)
from utils.speech_to_text import SpeechToText
from utils.scam_detector import ScamDetector

stt = SpeechToText()

text = stt.transcribe(path)

st.audio(uploaded)

st.markdown("## Transcript")

st.info(text)

scam = ScamDetector()

prediction = scam.predict(text)
from utils.database import Database
from utils.risk_calculator import RiskCalculator
from utils.report_generator import ReportGenerator

from datetime import datetime

risk, level = RiskCalculator.calculate(
    result["confidence"],
    prediction["confidence"]
)

st.metric("Risk Score", f"{risk}%")
st.progress(risk / 100)

if level == "HIGH":
    st.error(level)
elif level == "MEDIUM":
    st.warning(level)
else:
    st.success(level)
st.divider()

st.header("🎵 Audio Statistics")

stats = AudioStatistics.get_statistics(audio, sr)

c1, c2 = st.columns(2)

c3, c4 = st.columns(2)

c1.metric(
    "Duration",
    f"{stats['Duration (sec)']} sec"
)

c2.metric(
    "Sample Rate",
    stats["Sample Rate (Hz)"]
)

c3.metric(
    "RMS Energy",
    stats["RMS Energy"]
)

c4.metric(
    "Zero Crossing",
    stats["Zero Crossing Rate"]
)
st.divider()

st.header("📊 Audio Visualization")

st.pyplot(
    AudioVisualizer.plot_waveform(audio, sr)
)

st.pyplot(
    AudioVisualizer.plot_mel_spectrogram(audio, sr)
)

st.pyplot(
    AudioVisualizer.plot_mfcc(audio, sr)
)

st.pyplot(
    AudioVisualizer.plot_chroma(audio, sr)
)

st.pyplot(
    AudioVisualizer.plot_pitch(audio, sr)
)

db = Database()

db.insert(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    uploaded.name,
    result["prediction"],
    result["confidence"],
    text,
    prediction["prediction"],
    prediction["confidence"],
    risk
)

pdf = ReportGenerator()

pdf_path = pdf.generate(
    uploaded.name.split(".")[0],
    result["prediction"],
    result["confidence"],
    text,
    prediction["prediction"],
    prediction["confidence"],
    risk,
    level
)

with open(pdf_path, "rb") as file:
    st.download_button(
        "📄 Download Report",
        file,
        file_name=f"{uploaded.name}.pdf",
        mime="application/pdf"
    )

st.markdown("## Scam Detection")

if prediction["prediction"] == "Normal":

    st.success("Normal Conversation")

else:

    st.error(prediction["prediction"])

st.metric(

    "Scam Confidence",

    f"{prediction['confidence']}%"
)

st.markdown("## Prediction")

if result["prediction"] == "Real Voice":

    st.success(result["prediction"])

else:

    st.error(result["prediction"])

c1, c2 = st.columns(2)

c1.metric(
    "Voice Status",
    result["prediction"]
)

c2.metric(
    "Confidence",
    f"{result['confidence']}%"
)
st.progress(result["confidence"]/100)

st.subheader("📈 Prediction Probability")

df = pd.DataFrame({

    "Class": ["Real", "Fake"],

    "Probability": [

        result["real_probability"],

        result["fake_probability"]

    ]

})

fig = px.bar(

    df,

    x="Class",

    y="Probability",

    text="Probability",

    title="Deepfake Prediction Confidence"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.success("✅ Analysis Completed Successfully")
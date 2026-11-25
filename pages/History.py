from utils.ui import set_background

set_background()
from utils.header import header

header()
import streamlit as st
import pandas as pd

from utils.database import Database

st.title("📜 Detection History")

db = Database()

rows = db.fetch()

columns = [

    "ID",
    "Time",
    "Filename",
    "Prediction",
    "Confidence",
    "Transcript",
    "Scam",
    "Scam Confidence",
    "Risk"

]

df = pd.DataFrame(rows, columns=columns)

st.dataframe(
    df,
    use_container_width=True
)
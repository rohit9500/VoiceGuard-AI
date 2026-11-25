import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("dataset/scam/scam_dataset.csv")

X = df["text"]
y = df["label"]

pipeline = Pipeline([

    ("tfidf", TfidfVectorizer()),

    ("model", RandomForestClassifier(
        n_estimators=300,
        random_state=42
    ))

])

pipeline.fit(X, y)

joblib.dump(
    pipeline,
    "models/scam_classifier.pkl"
)

print("Scam Model Saved")
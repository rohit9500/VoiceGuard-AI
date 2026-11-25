import os
import sys
import joblib
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.audio_loader import AudioLoader
from utils.audio_preprocessing import AudioPreprocessor
from utils.feature_extraction import FeatureExtractor

# -----------------------------
# Dataset Paths
# -----------------------------
REAL_PATH = "dataset/deepfake/real"
FAKE_PATH = "dataset/deepfake/fake"

loader = AudioLoader()

X = []
y = []

print("Loading REAL audios...")

for file in os.listdir(REAL_PATH):

    if file.endswith(".wav"):

        path = os.path.join(REAL_PATH, file)

        audio, sr = loader.load_audio(path)

        audio = AudioPreprocessor.preprocess(audio, sr)

        features = FeatureExtractor.extract_features(audio, sr)

        X.append(features)
        y.append(0)

print("Loading FAKE audios...")

for file in os.listdir(FAKE_PATH):

    if file.endswith(".wav"):

        path = os.path.join(FAKE_PATH, file)

        audio, sr = loader.load_audio(path)

        audio = AudioPreprocessor.preprocess(audio, sr)

        features = FeatureExtractor.extract_features(audio, sr)

        X.append(features)
        y.append(1)

X = np.array(X)
y = np.array(y)

print("Dataset Shape :", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

print("Training Model...")

model.fit(X_train, y_train)

joblib.dump(model, "models/fake_voice_model.pkl")

joblib.dump((X_test, y_test), "models/test_data.pkl")

print("\nModel Saved Successfully!")
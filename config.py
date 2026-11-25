import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset Paths
DATASET_PATH = os.path.join(BASE_DIR, "dataset")

REAL_AUDIO_PATH = os.path.join(DATASET_PATH, "deepfake", "real")
FAKE_AUDIO_PATH = os.path.join(DATASET_PATH, "deepfake", "fake")

SCAM_DATASET = os.path.join(DATASET_PATH, "scam", "scam_dataset.csv")

# Models
MODEL_DIR = os.path.join(BASE_DIR, "models")

FAKE_MODEL = os.path.join(MODEL_DIR, "fake_voice_model.pkl")
SCAM_MODEL = os.path.join(MODEL_DIR, "scam_classifier.pkl")
EMOTION_MODEL = os.path.join(MODEL_DIR, "emotion_model.pkl")

# Reports
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# Assets
ASSETS = os.path.join(BASE_DIR, "assets")
import joblib

from utils.audio_loader import AudioLoader
from utils.audio_preprocessing import AudioPreprocessor
from utils.feature_extraction import FeatureExtractor


class FakeVoiceDetector:

    def __init__(self):

        self.model = joblib.load("models/fake_voice_model.pkl")

        self.loader = AudioLoader()


    def predict(self, audio_path):

        audio, sr = self.loader.load_audio(audio_path)

        audio = AudioPreprocessor.preprocess(audio, sr)

        features = FeatureExtractor.extract_features(audio, sr)

        prediction = self.model.predict([features])[0]

        probability = self.model.predict_proba([features])[0]

        real_prob = probability[0] * 100

        fake_prob = probability[1] * 100

        if prediction == 0:

            label = "Real Voice"

            confidence = real_prob

        else:

            label = "Fake Voice"

            confidence = fake_prob

        return {

            "prediction": label,

            "confidence": round(confidence,2),

            "real_probability": round(real_prob,2),

            "fake_probability": round(fake_prob,2)

        }
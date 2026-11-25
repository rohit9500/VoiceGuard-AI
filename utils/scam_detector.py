import joblib


class ScamDetector:

    def __init__(self):

        self.model = joblib.load(
            "models/scam_classifier.pkl"
        )

    def predict(self, text):

        prediction = self.model.predict([text])[0]

        probability = max(
            self.model.predict_proba([text])[0]
        ) * 100

        return {

            "prediction": prediction,

            "confidence": round(probability,2)

        }
import joblib

model = joblib.load("models/fake_voice_model.pkl")

print("Model Loaded Successfully")

print(model)
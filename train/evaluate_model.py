import joblib

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

model = joblib.load("models/fake_voice_model.pkl")

X_test, y_test = joblib.load("models/test_data.pkl")

pred = model.predict(X_test)

print("\nAccuracy :")

print(accuracy_score(y_test, pred))

print("\nClassification Report")

print(classification_report(y_test, pred))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, pred))
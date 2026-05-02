import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load training data
data = pd.read_csv("training_data.csv")

X = data["Feedback"]
y = data["Category"]

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "feedback_model.pkl")

print("Model trained and saved successfully!")
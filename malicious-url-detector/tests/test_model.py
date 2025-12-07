import pickle
import pandas as pd
import sys
import os

# Add parent directory to import feature_engineering
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from feature_engineering import build_feature_df

# Load your trained model
model = pickle.load(open("../models/model.pkl", "rb"))

# Define a list of test URLs (both benign and malicious)
test_urls = [
    "https://google.com",                         # expected benign
    "https://youtube.com",                        # expected benign
    "http://update-account-login.com",            # expected malicious
    "http://verifyinformation-login-now.info",    # expected malicious
    "https://random-check-info.net",              # mid-level suspicion
    "http://best-offers-today.net"                # slightly suspicious
]

print("\nRunning model tests...\n")

for url in test_urls:
    # Convert URL into features
    features = build_feature_df(pd.Series([url]))

    # Predict class
    prediction = model.predict(features)[0]

    # Confidence
    confidence = model.predict_proba(features)[0][prediction]

    # Human-readable label
    label = "Malicious" if prediction == 1 else "Benign"

    # Output results
    print(f"URL: {url}")
    print(f"Prediction: {label} (Confidence: {confidence:.2f})")
    print("-" * 50)

print("\nTest run complete.")
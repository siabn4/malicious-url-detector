import streamlit as st
import pickle
import pandas as pd
from feature_engineering import build_feature_df

# Load the trained machine learning model from the models folder
model = pickle.load(open("../models/model.pkl", "rb"))

# Title and description for the Streamlit web application
st.title("🔒 Malicious URL Detection System")
st.write("Enter a URL to check whether it is malicious or benign.")

# Text input box where the user enters a URL
url_input = st.text_input("URL:")

# When the user clicks the Analyze button, the model will make a prediction
if st.button("Analyze URL"):
    # Check if the user submitted an empty string
    if url_input.strip() == "":
        st.warning("Please enter a URL.")
    else:
        # Convert the input URL into a DataFrame of extracted features
        features = build_feature_df(pd.Series([url_input]))

        # Model predicts the class (0 = benign, 1 = malicious)
        prediction = model.predict(features)[0]

        # Probability/confidence score for the predicted class
        confidence = model.predict_proba(features)[0][prediction]

        # Display results to the user depending on prediction
        if prediction == 1:
            st.error(f" Malicious URL detected! (Confidence: {confidence:.2f})")
        else:
            st.success(f" URL appears safe. (Confidence: {confidence:.2f})")

        # Show the features extracted from the URL for transparency
        st.write("Extracted Features:")
        st.write(features)
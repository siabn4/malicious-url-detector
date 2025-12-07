import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
from feature_engineering import build_feature_df

# Load the dataset of URLs and labels (benign/malicious)
df = pd.read_csv("../data/urls.csv")

# Convert textual labels into numerical values: benign = 0, malicious = 1
df["label"] = df["label"].map({"benign": 0, "malicious": 1})

# Extract features using the feature engineering file
X = build_feature_df(df["url"])  # Feature matrix
y = df["label"]                 # Labels

# Split dataset into training (80%) and testing (20%) sets
# stratify=y keeps the class balance consistent
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create a Logistic Regression classifier and train it on the data
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Use the trained model to predict on the test set
preds = model.predict(X_test)

# Evaluate accuracy of the model
accuracy = accuracy_score(y_test, preds)
cm = confusion_matrix(y_test, preds)

print("Model Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)

# Save the trained model to the models folder so the Streamlit app can load it
pickle.dump(model, open("../models/model.pkl", "wb"))

print("Model saved to /models/model.pkl")
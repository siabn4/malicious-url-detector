# Malicious URL Detection System

## Project Overview
This project implements a machine learning-based system that classifies URLs as malicious or benign using engineered features extracted directly from the URL string. The project includes:

- A Python-based feature engineering module  
- A machine learning training pipeline using scikit-learn  
- A Streamlit web application for URL classification  
- A test script to verify model behavior and predictions  

This final product fulfills the **Target Product** defined in the project proposal.

---

## Repository Structure

malicious-url-detector/
│
├── code/
│ ├── feature_engineering.py # Extracts features from URLs
│ ├── train_model.py # Trains ML model and saves model.pkl
│ └── app.py # Streamlit UI for URL classification
│
├── data/
│ └── urls.csv # Dataset of benign/malicious URLs
│
├── models/
│ └── model.pkl # Saved trained Logistic Regression model
│
├── tests/
│ └── test_model.py # Tests feature extraction and predictions
│
├── docs/ # Optional documentation files
│
├── report/
│ └── project_report.docx # Final project report
│
└── README.md # This file

yaml
Copy code

---

## Installation and Setup

### 1. Install Dependencies
Run the following in your terminal:

pip install pandas scikit-learn numpy streamlit

shell
Copy code

### 2. Train the Machine Learning Model
Navigate into the code folder and execute:

cd code
python train_model.py

perl
Copy code

A trained model file, `model.pkl`, will be generated and saved in the `models/` directory.

### 3. Launch the Streamlit Application
From the `code` directory, run:

streamlit run app.py

yaml
Copy code

A browser window will open, allowing you to input URLs and view predictions.

---

## Running Tests

A test script is included to verify that:

- The model loads correctly  
- Feature extraction works as expected  
- Predictions are generated without errors  
- Confidence scores appear as intended  

Run the tests with:

cd tests
python test_model.py

yaml
Copy code

The script outputs prediction results and confidence values for several sample URLs.

---

## Dataset Description

The dataset used for training (`data/urls.csv`) contains two columns:

- `url`: The URL string  
- `label`: Either `benign` or `malicious`  

Benign URLs consist of legitimate, well-known domains, while malicious URLs include common phishing characteristics such as suspicious keywords, hyphens, misleading structures, and unusual top-level domains.

This small dataset is intentionally simple to match the scope of a 10-hour project.

---

## Technologies Used

- Python  
- pandas  
- scikit-learn  
- numpy  
- Streamlit  
- pickle  

---

## Target Audience

This project is designed for:

- Students learning about machine learning and cybersecurity  
- Individuals exploring URL analysis or phishing detection  
- Anyone wanting a simple, interactive demonstration of classical ML applied to security  

---

## Use of LLMs

Large Language Models were used to support:

- Debugging  
- Code explanations  
- Documentation writing  
- Structuring project components  
- Clarifying machine learning concepts  

---

## Notes

This system is an educational project and not intended for real-world cybersecurity defense.  
The model's accuracy and behavior are limited by the small dataset size 
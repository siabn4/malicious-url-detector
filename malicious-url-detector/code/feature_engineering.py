import re
import pandas as pd

# Extracts handcrafted features from a single URL string.
# These features help the ML model decide whether a URL looks malicious.
def extract_features(url):
    return {
        # Total number of characters in the URL
        "length": len(url),

        # Count of any digits in the URL
        "num_digits": sum(c.isdigit() for c in url),

        # Count of any characters that are not letters or numbers
        "num_special": sum(not c.isalnum() for c in url),

        # Whether the URL starts with HTTPS (considered more secure)
        "has_https": 1 if url.startswith("https") else 0,

        # Number of "/" characters — often higher in phishing URLs
        "num_subdirs": url.count("/"),

        # Check if the URL contains an IP address instead of a domain name
        "has_ip": 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,

        # Detect if common phishing-related keywords appear in the URL
        "contains_suspicious_words": 1 if any(
            word in url.lower() 
            for word in ["login", "verify", "secure", "update", "free"]
        ) else 0
    }

# Converts a list/Series of URLs into a full DataFrame of extracted features.
def build_feature_df(url_series):
    # Apply extract_features to each URL and return as a DataFrame
    features = [extract_features(u) for u in url_series]
    return pd.DataFrame(features)
from urllib.parse import urlparse
import pandas as pd
import re

# Load decoded URLs
decoded_csv = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/decoded_urls.csv"
decoded_data = pd.read_csv(decoded_csv)

# Function to preprocess URLs
def preprocess_url(url):
    if pd.isna(url) or not url.strip():
        return None, None, None, None
    try:
        parsed = urlparse(url)
        protocol = parsed.scheme
        domain = parsed.netloc
        path = parsed.path
        query = parsed.query
        return protocol, domain, path, query
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None, None, None, None

# Apply preprocessing
decoded_data[['protocol', 'domain', 'path', 'query']] = decoded_data['url'].apply(
    lambda x: pd.Series(preprocess_url(x))
)

# Save preprocessed data
decoded_data.to_csv("/Users/robert/Documents/Adv. Cyber Security/FinalProject/preprocessed_urls.csv", index=False)
print("URL preprocessing complete.")

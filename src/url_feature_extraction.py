import pandas as pd
import re

# Load preprocessed URLs
preprocessed_csv = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/preprocessed_urls.csv"
data = pd.read_csv(preprocessed_csv)

# Feature extraction functions
def count_special_chars(url):
    return len(re.findall(r"[@#?&=%]", url)) if pd.notna(url) else 0

def is_ip_address(domain):
    return bool(re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain)) if pd.notna(domain) else 0

# Apply feature extraction
data['url_length'] = data['url'].apply(lambda x: len(x) if pd.notna(x) else 0)
data['num_special_chars'] = data['url'].apply(count_special_chars)
data['is_ip'] = data['domain'].apply(is_ip_address)

# Save feature-engineered data
data.to_csv("/Users/robert/Documents/Adv. Cyber Security/FinalProject/feature_data.csv", index=False)
print("Feature extraction complete.")

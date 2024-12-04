from pyzbar.pyzbar import decode
from PIL import Image
import os
import pandas as pd

# Paths to QR code directories
base_dir = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/dataset"
benign_dir = os.path.join(base_dir, "benign")
malicious_dir = os.path.join(base_dir, "malicious")

# Function to decode QR codes
def decode_qr_codes(input_dir, label):
    data = []
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        try:
            decoded = decode(Image.open(file_path))
            if decoded:
                url = decoded[0].data.decode('utf-8')
                data.append({"url": url, "label": label})
            else:
                data.append({"url": None, "label": label})  # Handle empty QR codes
        except Exception as e:
            print(f"Error decoding {file}: {e}")
            data.append({"url": None, "label": label})  # Handle errors
    return data

# Decode both benign and malicious QR codes
benign_data = decode_qr_codes(benign_dir, "benign")
malicious_data = decode_qr_codes(malicious_dir, "malicious")

# Combine and save as a CSV
decoded_data = pd.DataFrame(benign_data + malicious_data)
decoded_data.to_csv("/Users/robert/Documents/Adv. Cyber Security/FinalProject/decoded_urls.csv", index=False)

print("QR code decoding complete.")

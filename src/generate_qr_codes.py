import os
import pandas as pd
import qrcode
import threading

# Paths
csv_file_path = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/reduced_dataset.csv"
output_dir = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/dataset"

# Directories for QR codes
benign_dir = os.path.join(output_dir, "benign")
malicious_dir = os.path.join(output_dir, "malicious")

# Create directories
os.makedirs(benign_dir, exist_ok=True)
os.makedirs(malicious_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv(csv_file_path)

# Separate the dataset into benign and malicious
benign_df = df[df['label'] == 'benign']
malicious_df = df[df['label'] == 'malicious']

# Function to generate QR codes
def generate_qr_codes(data, output_dir, label, max_count):
    count = 0
    for index, row in data.iterrows():
        if count >= max_count:
            break
        url = row['url']
        
        # Create the QR code
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code with the specified naming convention
        file_path = os.path.join(output_dir, f"{label}_{index + 1}.png")
        img.save(file_path)
        count += 1

# Maximum QR codes per category
max_count = 75000

# Create threads for benign and malicious
benign_thread = threading.Thread(target=generate_qr_codes, args=(benign_df, benign_dir, "benign", max_count))
malicious_thread = threading.Thread(target=generate_qr_codes, args=(malicious_df, malicious_dir, "malicious", max_count))

# Start the threads
benign_thread.start()
malicious_thread.start()

# Wait for both threads to complete
benign_thread.join()
malicious_thread.join()

print("QR Code generation complete.")

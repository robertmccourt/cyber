import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
base_dir = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/dataset"
output_dir = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/split_dataset"

benign_dir = os.path.join(base_dir, "benign")
malicious_dir = os.path.join(base_dir, "malicious")

# Create output directories for train, val, and test splits
for split in ['train', 'val', 'test']:
    for category in ['benign', 'malicious']:
        os.makedirs(os.path.join(output_dir, split, category), exist_ok=True)

# Function to split and copy files
def split_and_copy_files(src_dir, output_dir, split_sizes):
    files = sorted(os.listdir(src_dir))  # Sort to ensure consistent order
    train_files, test_files = train_test_split(files, test_size=split_sizes['test'], random_state=42)
    train_files, val_files = train_test_split(train_files, test_size=split_sizes['val'] / (1 - split_sizes['test']), random_state=42)

    # Copy files to their respective directories
    for file in train_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(output_dir, 'train', os.path.basename(src_dir)))
    for file in val_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(output_dir, 'val', os.path.basename(src_dir)))
    for file in test_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(output_dir, 'test', os.path.basename(src_dir)))

# Split sizes for train, val, and test
split_sizes = {'train': 0.7, 'val': 0.2, 'test': 0.1}

# Split and copy files for both benign and malicious datasets
split_and_copy_files(benign_dir, output_dir, split_sizes)
split_and_copy_files(malicious_dir, output_dir, split_sizes)

print("Dataset successfully split into training, validation, and testing sets!")

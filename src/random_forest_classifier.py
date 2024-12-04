import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load feature data
feature_data_csv = "/Users/robert/Documents/Adv. Cyber Security/FinalProject/feature_data.csv"
data = pd.read_csv(feature_data_csv)

# Prepare features and labels
X = data[['url_length', 'num_special_chars', 'is_ip']].fillna(0)  # Replace NaN with 0
y = data['label'].apply(lambda x: 1 if x == 'malicious' else 0)  # Convert labels to binary

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Performance:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

import json
import pandas as pd

# Load JSON file
with open("train_fraud_labels.json", "r") as f:
    fraud_data = json.load(f)

# Auto-detect the correct structure
if isinstance(fraud_data, dict):
    if "root" in fraud_data and "target" in fraud_data["root"]:
        fraud_labels = fraud_data["root"]["target"]
    elif "target" in fraud_data:
        fraud_labels = fraud_data["target"]
    else:
        raise KeyError("Could not find 'root' or 'target' in JSON structure.")
elif isinstance(fraud_data, list):
    raise ValueError("JSON file is a list, please provide a sample structure.")

# Convert to DataFrame
fraud_df = pd.DataFrame(list(fraud_labels.items()), columns=["Transaction ID", "Fraud Label"])

# Save as CSV
fraud_df.to_csv("fraud_labels.csv", index=False)

print("Conversion complete! File saved as fraud_labels.csv")

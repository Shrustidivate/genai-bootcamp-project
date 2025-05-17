# day1_pandas_basics.py

import pandas as pd

# Load CSV file
df = pd.read_csv("sample_data.csv")

# Show first 5 rows
print("🔹 First 5 Rows:")
print(df.head())

# Remove null values
df_clean = df.dropna()
print("\n🔹 Cleaned Data (No nulls):")
print(df_clean.head())

# Describe numeric columns
print("\n🔹 Summary Statistics:")
print(df_clean.describe())

# Count unique values in a column (example: "Category")
if "Category" in df.columns:
    print("\n🔹 Unique Categories:")
    print(df["Category"].value_counts())

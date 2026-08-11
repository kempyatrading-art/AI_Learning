# Day 4 — Data Cleaning

#Step 1 — Put this data into duplicate_sensor_data.csv
#Step 2 — Create duplicate_data.py

import pandas as pd 

sensor_data = pd.read_csv("D:/AI_Learning/day4_pandas/duplicate_sensor_data.csv")

print("Sensor Dataset:")
print(sensor_data)

# identify shape of DataFrame:
print("\nDataset Shape :")
print(sensor_data.shape)

# Step 3 — Detect duplicate records
print("\nDuplicate Records Count:")
print(sensor_data.duplicated().sum())

# Step 4 — Display only duplicate rows
duplicates = sensor_data[sensor_data.duplicated()]

print("\nDuplicate Rows:")
print(duplicates)

#Step 5 — Remove duplicates
cleaned_data = sensor_data.drop_duplicates()

print("\nAfter Removing Duplicates :")
print(cleaned_data.shape)
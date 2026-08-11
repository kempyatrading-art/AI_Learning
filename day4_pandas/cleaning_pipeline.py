# Building a Real Data-Cleaning Pipeline :-

"""
A Data-Cleaning Pipeline is an automated, multi-step workflow that transforms raw, 
unrefined data into a validated, clean format ready for machine learning models. Crucially,
a production pipeline flags and segregates invalid entries rather than destroying raw records, 
preserving auditability while ensuring downstream models receive high-quality data. 
"""
# Step 1 — Create a new file :- day4_pandas/cleaning_pipeline.py
#Keep invalid_data.py unchanged. It's useful as our validation/testing script.

#Step 2 — Load the data :-
import pandas as pd 

sensor_data = pd.read_csv ("D:/AI_Learning/day4_pandas/duplicate_sensor_data.csv")

print("Original Dataset Shap :")
print(sensor_data.shape)

# Step 3 — Convert timestamp :-
sensor_data["timestamp"] =pd.to_datetime(sensor_data["timestamp"])
print("\n",sensor_data["timestamp"].dtype)

# Step 4 — Remove exact duplicates
cleaned_data =sensor_data.drop_duplicates().copy()
print("\nAfter Removing Duplicates : ")
print(cleaned_data.shape)

# Step 5 — Create validation masks

#Battery
invalid_battery = (
    (cleaned_data["battery"]<0)|
    (cleaned_data["battery"]>100)
)

#Temperature 
invalid_temperature =(
    (cleaned_data["temperature"]<-20)|
    (cleaned_data["temperature"]>120)
)

#Vibration 
invalid_vibration =cleaned_data["vibration"]<0

#Current 
invalid_current =cleaned_data["current"]<0

#Status
valid_status =["Running","Offline"]
invalid_status =~cleaned_data["status"].isin(valid_status)

# Step 6 — Create a data-quality flag 
cleaned_data["data_quality"] ="Valid"

invalid_any =(
    invalid_battery |
    invalid_temperature |
    invalid_vibration |
    invalid_current |
    invalid_status
)

cleaned_data.loc[invalid_any,"data_quality"] = "Invalid"

# Step 7 — See the invalid records
print("\nInvalid Records :")
print(
    cleaned_data[
        cleaned_data["data_quality"] == "Invalid"
    ]
)

# Step 8 — Count valid vs invalid :-
print("\nData Quality Summary :")
print(cleaned_data["data_quality"].value_counts())

# Step 9 — Create a clean dataset 
# Now we can create a separate DataFrame containing only records that passed our validation rules:

final_data =cleaned_data[cleaned_data["data_quality"] == "Valid"].copy()

print("\nFinal Clean Dataset :")
print(final_data)

print("\nFinal Dataset Shape :")
print(final_data.shape)

# Step 10 — Save the cleaned dataset
final_data.to_csv("D:/AI_Learning/day4_pandas/cleaned_sensor_data.csv",index=False)
#to_csv() exports a Pandas DataFrame to a CSV file.
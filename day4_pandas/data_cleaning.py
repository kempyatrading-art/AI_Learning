# Data Cleaning :-
# Data cleaning is the process of detecting, correcting, removing, or handling inaccurate, incomplete, 
# ,duplicated, or inconsistent data before analysis or machine learning.

#code 1

import pandas as pd 

# Load the messy sensor dataset
sensor_data =pd.read_csv("D:/AI_Learning/day4_pandas/messy_sensor_data.csv")

print("Messy Sensor Data :")
print(sensor_data)

sensor_data["timestamp"]=pd.to_datetime(sensor_data["timestamp"])
print("\n")
print(sensor_data.info())

print("\nMissing Values :")
print(sensor_data.isna())

print("\nMissing Values Per Column:")
print(sensor_data.isna().sum())

# Method 1 — Remove rows:-
# dropna() removes rows or columns containing missing values.

# Experiment 1: Remove rows with missing values
cleaning_data=sensor_data.dropna()
print("\nAfter Removing Rows With Missing Values : ")
print(cleaning_data)

# Method 2 — Fill with the Mean :-
#For numerical sensor data, one option is replacing a missing value with the column's average.

#copy() :-creates an independent copy of a DataFrame so that changes can be made without modifying the original dataset.

# Experiment 2: Fill missing battery values with mean
mean_filled =sensor_data.copy()  # creates an independent copy of a DataFrame 

mean_filled ["battery"] = mean_filled["battery"].fillna(mean_filled ["battery"].mean())
print("\nBattery after Mean Filling :")
print(mean_filled )

#Method 3 — Forward Fill
# Forward filling (.ffill()) replaces a missing value with the most recent previous non-missing value

# Experiment 3: Forward fill missing vibration values
forward_filled =mean_filled.copy() # creates an independent copy of a DataFrame 

forward_filled ["vibration"] = (forward_filled .groupby("robot_id")["vibration"].ffill()) # we used .groupby because we cant fill other device data in this device so we .groupby("robot_id")["vibration"].ffill()
print("\nVibration after Forward Fill:")
print(forward_filled)


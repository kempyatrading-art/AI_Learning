# CSV (Comma-Separated Values) is a simple tabular file format used to store structured data in rows and columns.
# pd.read_csv() reads a CSV file and returns a Pandas DataFrame.
#Example code  
"""
import pandas as pd

# pd.read_csv() loads a CSV file into a Pandas DataFrame
df = pd.read_csv("filepath_or_filename.csv")  

"""
# code 1

# Step 2: Create the Python Script :-

import pandas as pd 

sensor_data = pd.read_csv("D:\AI_Learning\day4_pandas\robot_sensor_data.csv")
print("Robot Sensor Data :")
print(sensor_data)

# 1. Inspect first 5 rows
print("\nFirst 5 Record :")
print(sensor_data.head())

# 2. Inspect last 5 rows
print("\nLast 5 Record :")
print(sensor_data.tail())

# 3. View dataset dimensions
print("\nDataset Shape:")
print(sensor_data.shape)

# 4. List all column headers
print("\nColumns:")
print(sensor_data.columns)

# 5. Summary of structure and data types
print("\nDataset Information :")
sensor_data.info()

# Convert the 'timestamp' column from string to datetime64
sensor_data["timestamp"] = pd.to_datetime(sensor_data["timestamp"])

# Verify the updated data types
print("\nUpdated Dataset Information:")
sensor_data.info()

# 1. Check data type of column
print("\nTimestamp Data Type :")
print(sensor_data["timestamp"].dtype)

# 2. Get the latest record timestamp
print("\nLatest Sensor Record :")
print(sensor_data["timestamp"].max())

# 3. Get the earliest record timestamp
print("\nEarliest Sensor Record :")
print(sensor_data["timestamp"].min())

#  Average battery for each robot :-
average_battery = sensor_data.groupby("robot_id")["battery"].mean()
print("\nAverage Battery By Robot :")
print(average_battery)

# Average temperature by robot :-
average_temperature = sensor_data.groupby("robot_id")["temperature"].mean()
print("\nAverage Temperature By Robot :")
print(average_temperature)

# Multiple Aggregations :-
robot_summary = sensor_data.groupby("robot_id").agg({
    "battery":["mean","min","max"],
    "temperature":["mean","max"],
    "vibration":["mean","max"]
})

print("\nRobot Sensor Summary :")
print(robot_summary)
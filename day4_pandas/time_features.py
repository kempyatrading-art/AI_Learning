"""
Feature engineering
Feature engineering is the process of creating useful input variables from raw data.
"""

# Next topic: Time-Based Feature Engineering

import pandas as pd 

sensor_data = pd.read_csv("D:/AI_Learning/day4_pandas/cleaned_sensor_data.csv")
sensor_data["timestamp"]=pd.to_datetime(sensor_data["timestamp"])
print("Original Data :")
print(sensor_data)
print("\nshape:",sensor_data.shape)

# Step 2 — Sort by robot and time
#This is very important before calculating changes.

sensor_data=sensor_data.sort_values(["robot_id","timestamp"])
print("\n Sorted sensor Data :")
print(sensor_data)

# Time-series calculations must generally be performed in chronological order.

#Step 3 — Calculate battery change
#Now we'll use one of the most useful Pandas functions for time-series data: diff()

sensor_data["battery_change"]=(sensor_data.groupby("robot_id")["battery"].diff())
print("\nBattery Change")
print(sensor_data[["timestamp","robot_id","battery","battery_change"]])

#Step 4 — Calculate temperature change
#Now do the same thing:
sensor_data["temperature_change"]=(sensor_data.groupby("robot_id")["temperature"].diff())
print("\nTemperature change")
print(sensor_data[["timestamp","robot_id","temperature","temperature_change"]])

#Now we can see whether each robot's temperature is increasing or decreasing.

#Step 5 — Calculate vibration change
sensor_data["vibration_change"]=(sensor_data.groupby("robot_id")["vibration"].diff())
print("\nVibration change")
print(sensor_data[["timestamp","robot_id","vibration","vibration_change"]])

#Step 6 — Calculate current change
sensor_data["current_change"]=(sensor_data.groupby("robot_id")["current"].diff())
print("\ncurrent change")
print(sensor_data[["timestamp","robot_id","current","current_change"]])

"""
diff() : Calculates the difference between the current observation and the previous observation."""

# Next: calculate time between readings
# Time difference between consecutive readings for each robot

sensor_data["time_difference"]=(sensor_data.groupby("robot_id")["timestamp"].diff())
print("\n Time Difference :")
print(sensor_data[["timestamp","robot_id","time_difference"]])

"""Time difference:-
The amount of time elapsed between two consecutive observations."""

sensor_data["time_minutes"]=(sensor_data["time_difference"].dt.total_seconds()/60)
print("\n Time Difference In Minutes :")
print(sensor_data[["timestamp","robot_id","time_difference","time_minutes"]])

# dt.total_seconds() converts a Pandas timedelta into seconds.

# Then: Battery Consumption Rate 
#Now we can combine the two things we just learned:

sensor_data["battery_rate"]=(sensor_data["battery_change"] / sensor_data["time_minutes"])
print("\nBattery Consumption Rate :")
print(sensor_data[["timestamp","robot_id","battery_change","time_minutes","battery_rate"]])


# Then: temperature  Rate 

sensor_data["temperature_rate"]=(sensor_data["temperature_change"] / sensor_data["time_minutes"])
print("\nTemperature change Rate :")
print(sensor_data[["timestamp","robot_id","temperature_change","time_minutes","temperature_rate"]])

"""Temperature Rate :-
Measures how quickly the robot's temperature changes over time."""

# Then: vibration  Rate 

sensor_data["vibration_rate"]=(sensor_data["vibration_change"] / sensor_data["time_minutes"])
print("\nVibration change Rate :")
print(sensor_data[["timestamp","robot_id","vibration_change","time_minutes","vibration_rate"]])

# Then: current  Rate 

sensor_data["current_rate"]=(sensor_data["current_change"] / sensor_data["time_minutes"])
print("\nCurrent change Rate :")
print(sensor_data[["timestamp","robot_id","current_change","time_minutes","current_rate"]])


# Day 4 — Pandas: Rolling Average

# Next: Rolling average for Temperature
sensor_data["temperature_rolling_mean"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nTemperature Rolling Mean :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_mean"]])

# Next: Rolling average for vibration
sensor_data["vibration_rolling_mean"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nVibration Rolling Mean :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_mean"]])

# Next: Rolling average for Current
sensor_data["current_rolling_mean"]=(sensor_data.groupby("robot_id")["current"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nCurrent Rolling Mean :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_mean"]])

# Next: Rolling average for Battery
sensor_data["battery_rolling_mean"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nBattery Rolling Mean :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_mean"]])

"""rolling(3) means:
Take the current value and the previous 2 values for the same robot, then calculate their average."""



# Next: Rolling Standard Deviation

# Next: Rolling Standard Deviation for Temperature
sensor_data["temperature_rolling_std"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).std().reset_index(level=0,drop=True))
print("\nTemperature Rolling std :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_std"]])

# Next: Rolling Standard Deviation for vibration
sensor_data["vibration_rolling_std"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).std().reset_index(level=0,drop=True))
print("\nVibration Rolling std :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_std"]])

# Next: Rolling Standard Deviation for Current
sensor_data["current_rolling_std"]=(sensor_data.groupby("robot_id")["current"].rolling(3).std().reset_index(level=0,drop=True))
print("\nCurrent Rolling std :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_std"]])

# Next: Rolling Standard Deviation for Battery
sensor_data["battery_rolling_std"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).std().reset_index(level=0,drop=True))
print("\nBattery Rolling std :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_std"]])



# 1. Rolling minimum — .rolling().min()

# Next: Rolling minimum for Temperature
sensor_data["temperature_rolling_min"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).min().reset_index(level=0,drop=True))
print("\nTemperature Rolling min :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_min"]])

# Next: Rolling minimum for vibration
sensor_data["vibration_rolling_min"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).min().reset_index(level=0,drop=True))
print("\nVibration Rolling min :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_min"]])

# Next: Rolling minimumn for Current
sensor_data["current_rolling_min"]=(sensor_data.groupby("robot_id")["current"].rolling(3).min().reset_index(level=0,drop=True))
print("\nCurrent Rolling min :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_min"]])

# Next: Rolling minimum for Battery
sensor_data["battery_rolling_min"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).min().reset_index(level=0,drop=True))
print("\nBattery Rolling min :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_min"]])


#2. Rolling maximum — .rolling().max()

# Next: Rolling maximum for Temperature
sensor_data["temperature_rolling_max"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).max().reset_index(level=0,drop=True))
print("\nTemperature Rolling max :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_max"]])

# Next: Rolling maximum for vibration
sensor_data["vibration_rolling_max"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).max().reset_index(level=0,drop=True))
print("\nVibration Rolling max :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_max"]])

# Next: Rolling maximum for Current
sensor_data["current_rolling_max"]=(sensor_data.groupby("robot_id")["current"].rolling(3).max().reset_index(level=0,drop=True))
print("\nCurrent Rolling max :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_max"]])

# Next: Rolling maximum for Battery
sensor_data["battery_rolling_max"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).max().reset_index(level=0,drop=True))
print("\nBattery Rolling max :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_max"]])
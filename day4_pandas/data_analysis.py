# Data Analysis with Pandas

"""
1. Introduction to Data Analysis with Pandas :-
Data analysis involves extracting meaningful insights from cleaned data rather than just preparing or cleaning it.
In industrial monitoring, robotics, IoT, 
and trading, data analysis allows you to detect trends, spot anomalies, and understand component behavior.
"""
# Descriptive statistics = methods used to summarize and understand a dataset.
"""
Important Pandas methods:

mean() → average
median() → middle value
min() → smallest value
max() → largest value
std() → standard deviation
count() → number of observations
describe() → generates several statistics together

"""
#Step 1 — Load our cleaned data

import pandas as pd 

sensor_data =pd.read_csv("D:/AI_Learning/day4_pandas/cleaned_sensor_data.csv")
print("Cleaned Robot Sensor Data:")
print(sensor_data)

print("\nDataset Shape :")
print(sensor_data.shape)

# Step 2 — Basic statistics
print("\nBattery Statistics :")
print("Average:",sensor_data["battery"].mean())
print("Minimum:",sensor_data["battery"].min())
print("Maximum:",sensor_data["battery"].max())

print("\nTemperature Statistics :")
print("Average:",sensor_data["temperature"].mean())
print("Minimum:",sensor_data["temperature"].min())
print("Maximum:",sensor_data["temperature"].max())

print("\nVibration Statistics :")
print("Average:",sensor_data["vibration"].mean())
print("Minimum:",sensor_data["vibration"].min())
print("Maximum:",sensor_data["vibration"].max())

"""
print("\n Find more vibrating and remove duplicates ")
sensor_data["vibration"] = sensor_data["vibration"].max() 
print(sensor_data[["robot_id","vibration"]].drop_duplicates()) 
"""
# Step 3 — Use describe() :-
print("\nComplete Numerical Statistics :")
print(sensor_data[["battery","temperature","vibration","current"]].describe())

"""describe() is extremely useful when you receive a new dataset and don't yet know what it looks like.
For example, when you eventually load:
a trading database
machine-production CSV
robot sensor logs
an Excel file
a SQLite database

"""

# Next: Robot-by-Robot Analysis

# Robot-by-Robot Analysis
robot_summary =sensor_data.groupby("robot_id").aggregate({
    "battery":["mean","min","max"],
    "temperature":["mean","max"],
    "vibration":["mean","max"],
    "current":["mean","max"]
})
print("\n"+"="*60)
print("ROBOT HEALTH SUMMARY")
print("="*60)

print(robot_summary)

# Aggregation :-
#Aggregation means combining multiple observations into a summary statistic such as mean, minimum, maximum, or sum.


#Then calculate battery decline
battery_change =sensor_data.groupby("robot_id")["battery"].agg(["first","last"])
battery_change["battery_drop"]=(battery_change["first"]-battery_change["last"])

print("\n"+"="*60)
print("BATTERY CHANGE")
print("="*60)

print(battery_change)

"""
aggregation :-
Aggregation means combining multiple observations into a summary statistic such as mean, minimum, maximum, or sum.
"""
#Next: Multi-Condition Robot Risk Detection
"""
Now we're going to create a simple rule-based health assessment.

This is not machine learning yet.

We're building the kind of logic that could later become a baseline against which we compare an ML model.

"""
# Robot Risk Detection
robot_health=sensor_data.groupby("robot_id").agg(
    average_battery = ("battery","mean"),
    average_temperature =("temperature","mean"),
    average_vibration =("vibration","mean"),
    average_current =("current","mean")
)
robot_health["risk_score"]=0

robot_health.loc[robot_health["average_battery"]<30,"risk_score"]+=1
robot_health.loc[robot_health["average_temperature"]>75,"risk_score"]+=1
robot_health.loc[robot_health["average_vibration"]>4,"risk_score"]+=1
robot_health.loc[robot_health["average_current"]>5,"risk_score"]+=1

print("\n"+"="*60)
print("ROBOT RISK ANALYSIS")
print("="*60)

print(robot_health)

"""
What is a risk score?
A risk score is a numerical value representing how many warning conditions a system has detected."""
import pandas as pd

sensor_data = pd.read_csv("D:/AI_Learning/day4_pandas/duplicate_sensor_data.csv")

print("Dataset Shape:")
print(sensor_data.shape)

# 1. Detect invalid battery percentage (< 0 or > 100)
invalid_battery = sensor_data[
    (sensor_data["battery"]<0)|
    (sensor_data["battery"]>100)
]
print("\nInvalid Battery Records :")
print(invalid_battery[["timestamp", "robot_id", "battery"]])

# 2. Detect invalid vibration (< 0)
invalid_vibration = sensor_data[
    (sensor_data["vibration"]<0)
]
print("\nInvalid Vibration Record :")
print(invalid_vibration[["timestamp","robot_id","vibration"]])


# 3. Detect invalid current (< 0)
invalid_current = sensor_data[
    sensor_data["current"] < 0
]
print("\nInvalid Current Records:")
print(invalid_current[["timestamp","robot_id","current"]])

# 4. Detect invalid temperature (< -20 or > 120)
invalid_temperature = sensor_data[
    (sensor_data["temperature"]<-20) |
    (sensor_data["temperature"]>120)
]
print("\nInvalid Temperature Record :")
print(invalid_temperature[["timestamp","robot_id","temperature"]])

# 5. Detect invalid status (Not 'Running' or 'Offline')
valid_status = ["Running","Offline"]
invalid_status = sensor_data[
    ~sensor_data["status"].isin(valid_status)
]
print("\nInvalid Status Record :")
print(invalid_status[["timestamp","robot_id","status"]])
#isin() checks whether values belong to a specified set of allowed values .
#The ~ means NOT.


# Next: Build a Validation Report :-
print("\n"+"="*40)
print("DATA VALIDATION REPORT ")
print("="*40)

print("Invalid Battery      :",len(invalid_battery))
print("Invalid Temperature  :",len(invalid_temperature))
print("Invalid Vibration    :",len(invalid_vibration))
print("Invalid Current      :",len(invalid_current))
print("Invalid Status       :",len(invalid_status))

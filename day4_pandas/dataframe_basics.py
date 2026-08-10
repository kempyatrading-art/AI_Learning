# CODE 1
"""
import pandas as pd  

robot_data= {
    "Robot_ID":[101,102,103,104,105],
    "Battery":[92,87,95,61,15],
    "Temperature":[45,48,43,60,82],
    "Status":["Running","Offline","Running","Running","Offline"]
}
robots =pd.DataFrame(robot_data)
print("Robot Fleet Data:")
print(robots)

# Access a Column

print("\nBattery Column:")
print(robots["Battery"])

print("\nBattery Column With ROBOT ID :")
print(robots[["Robot_ID","Battery"]])

"""
# CODE 2

import pandas as pd  

robot_data= {
    "Robot_ID":[101,102,103,104,105],
    "Battery":[92,87,95,61,15],
    "Temperature":[45,48,43,60,82],
    "Status":["Running","Offline","Running","Running","Offline"]
}
robots =pd.DataFrame(robot_data)               #____________DataFrame_____________
print("Robot Fleet Data:")
print(robots)

low_battery =  robots[robots["Battery"]<20]
print("\nLow Battery Robots:")
print (low_battery)

high_temp =robots[robots["Temperature"]>=75]
print("\nHigh temperature:")
print(high_temp)

offline_robot =robots[robots["Status"]=="Offline"]
print("\nOffline robots:")
print(offline_robot)

running_robot = robots[robots["Status"]=="Running"]
print("\nRunning robots:")
print(running_robot)

# Critical alert check (AND)
critical_robots =robots[
    (robots["Battery"]<20) & (robots["Temperature"]>75)
]
print("\nCritical Robots:")
print(critical_robots)

# Warning alert check (OR)
warning_robots =robots[
    (robots["Battery"]<20) | (robots["Temperature"]>75)
]

print("\nWarning alert Robots :")
print(warning_robots)

# Sorts by Battery in ascending order (default)
print("\nRobots Sorted By Battery :")
print(robots.sort_values("Battery"))

# Sorts by Battery in descending order
print("\nRobots Sorted By Battery according to descending order : ")
print(robots.sort_values("Battery",ascending =False) )

# DataFrame Aggregation :-

print("\n Robot Fleet Statistics","\n"+"="*30)

print("Average Battery:",robots["Battery"].mean(),"%")
print("Maximum Battery:",robots["Battery"].max(),"%")
print("Minium Battery :",robots["Battery"].min(),"%")
print("Total Battery  :",robots["Battery"].sum(),"%")
print("Robot Count    :",robots["Robot_ID"].count())
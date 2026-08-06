# arrays.py- Mini Challenge :
"""
import numpy as np
attendance = np.array([95,87,100,76,92])

print("all attendance :",attendance)

print("Highest Attendance :",np.max(attendance))
print("Lowest Attendance :",np.min(attendance))
print("Sum of all Attendance :",np.sum(attendance))
#print("Average Attendance :",np.mean(attendance))
print(f"Average Attendance : {np.mean(attendance):.2f}") #You'll use formatting like :.2f a lot when displaying percentages, ML model accuracy, and financial values.

"""
"""
#Mini Project

import numpy as np 
scores = np.array ([75,82,91,68,88,95,79])

print ("ALL Scores :",scores)

print("Highest Score :",np.max(scores))
print("Lowest Score :",np.min(scores))
print(f"Average Score:{np.mean(scores):.2f}")
print("Median Score :",np.median(scores))
print("Standard Deviation :",np.std(scores))
print("Variance :",np.var(scores))
"""
# Project: Robot Fleet Analytics Dashboard :-

import numpy as np 
robot_fleet = np.array([
    [101,92,45,1],
    [102,87,48,0],
    [103,95,43,1],
    [104,61,60,1],
    [105,15,82,0]
])

print("="*40)
print("       ROBOT FLEET DASHBOARD ")
print("="*40)

# Step 2: Loop and display individual robot status
running_count = 0
offline_count = 0
    
for robot in robot_fleet :
    robot_id = robot [0]
    battery= robot [1]
    motor_temp = robot [2]
    status_code = robot [3]
    
    if status_code == 1:
        status_str ="Running"
        running_count +=1
    if status_code == 0:
        status_str ="Offline"
        offline_count +=1
        
    print("\nRobot ID  :",robot_id)    
    print("Battery     :",battery ,"%")
    print("Temperature :",motor_temp,"°C")
    print("Status      :",status_str)
    print("-"*40)
        
# Step 3: Fleet Statistics using NumPy Slicing

avg_battery = np.mean (robot_fleet [:,1])
max_temp = np.max(robot_fleet [:,2])
total_robot = len(robot_fleet [:,0])

print("\n"+"="*40)
print("FLEET SUMMARY")
print("\n"+"-"*15)
print("Total Robot :", total_robot)
print("Running Robots :",running_count)
print("Offline Robots :",offline_count)
print("Average Battery :", avg_battery,"%")
print("Highest Temperature :",max_temp,"°C")

# Step 4: Critical Robot Detection
print("\n"+"="*40)
print("CRITICAL ROBOTS") 
print("-"*15)

for robot in robot_fleet :
    robot_id = robot[0]
    battery= robot[1]
    motor_temp = robot[2]
    status_code = robot[3]
    
    # Check if robot has any critical condition
    if battery <= 20 or motor_temp >= 75 or status_code == 0:
        print("Robot ID :",robot_id)
    
        if battery <= 20 :
            print("⚠ Battery Low")
            
        if motor_temp >= 75 :
            print("⚠ Motor Overheating")
            
        if status_code == 0:
            print("⚠ Offline")
            
            







    
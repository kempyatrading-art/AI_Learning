"""
matrix.py

This is one of the most important topics in AI.

Almost every machine learning algorithm uses matrices.

Neural networks?
👉 Matrices

Computer Vision?
👉 Matrices

Robotics?
👉 Matrices

Transformers (like ChatGPT)?
👉 Huge matrices
"""
# Step 1 — Create Your First Matrix
"""
import numpy  as np 
factory_sensor_data = np.array([
    [32.5,45.2,101.3],
    [33.1,44.8,100.9],
    [31.9,45.5,101.8]
])
print(factory_sensor_data)

# Step 2 — Check Matrix Shape

print("Shape :",np.shape(factory_sensor_data))

# Step 3 — Access Data 

print("First Reading :",factory_sensor_data[0])
print("Temperature :",factory_sensor_data[0,0])
print("Humidity :",factory_sensor_data[0,1])
print("pressure :",factory_sensor_data[0,2])
"""
# code 2

"""
import numpy as np 
robot_status = np.array([
    [101,92,45],
    [102,87,48],
    [103,95,43]
])

print(robot_status)
print("\nshape :",np.shape(robot_status))
print ("\nBattery of robot ID 102 :",robot_status[1,1],"%")
print("Motor temperature of Robot ID 103 :",robot_status[2,2],"°c")

#using import for access data of robot_status :
    
Robot_ID = int(input("\nRobot id :"))

if Robot_ID == 101:
    print ("\nRobot Battery :",robot_status[0,1],"%")
    print ("Robot Motor_temp :",robot_status[0,2],"°c")
    
elif Robot_ID ==102 :
    print ("\nRobot Battery :",robot_status[1,1],"%")
    print ("Robot Motor_temp  :",robot_status[1,2],"°c")

elif Robot_ID ==103 :
    print ("\nRobot Battery :",robot_status[2,1],"%")
    print ("Robot Motor_temp:",robot_status[2,2],"°c")
    
else:
    print("\nRobot ID not found.")
    
"""
#code : 3 -

"""
import numpy as np 
robot_status = np.array([
    [101,92,45],
    [102,87,48],
    [103,95,43]
])

print("Robot Monitoring System")
print("-" * 30)
print("\nshape :",np.shape(robot_status))
print ("\nBattery of robot ID 102 :",robot_status[1,1],"%")
print("Motor temperature of Robot ID 103 :",robot_status[2,2],"°c")

#using import for access data of robot_status :
    
Robot_ID = int(input("\nRobot id :"))
found = False
for robot in robot_status :
    if robot[0] == Robot_ID :

        print("\nRobot Found")
        print("Robot ID :", robot[0])
        print ("\nRobot Battery :",robot[1],"%")
        print ("Robot Motor_temp :",robot[2],"°c")
        
        found = True
        break   
    
if not found :
    print("\nRobot ID not found.")
    
"""
#code : 4 -

import numpy as np 
robot_status = np.array([
    [101,92,45,1],
    [102,87,48,0],
    [103,95,43,1],
    [104,61,60,1],
    [105,15,82,0]
])

Robot_ID = int(input("Enter the ROBOT ID :"))
found = False 
for robot in robot_status :
    if Robot_ID == robot [0]:
        found = True
        
        print("="*35)
        print ("ROBOT HEALTH REPORT")
        print("="*35)
        
        print ("\nRobot found")
        print("Robot ID :",Robot_ID)
        print("Motor Temp :",robot[2],"°C")
        print("Battery :",robot[1],"%")
        
        if robot [1]<= 20:
            print("\n⚠ Battery critically low")
                
        if robot [2]>=75:
                print ("⚠ Motor overheating")  
                
        if robot [3] == 0 :
            status = "⚠ Robot is Offline"
            print(status)
            
        else:
            print ("\n✅ Robot operating normally")
            
        break
            
if not found:
    print("❌ Robot ID not found.")
            
        
        

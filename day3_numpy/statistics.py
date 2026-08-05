#Step 1 — Mean
"""
import numpy as np 
marks = np.array ([85,92,40,88,95])
print("Marks :",marks)
print("Mean :",np.mean(marks))

# Step 2 — Median -

print("Median :",np.median(marks))

# Step 3 — Standard Deviation -

print ("Standard Deviation :",np.std(marks))

# Step 4 — Variance -

print ("variance :",np.var(marks)) 

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
#example code : Since goal is AI + Robotics + Automation, I'll use examples from:

import numpy as np
motor_speed = np.array([1200, 1180, 1210, 1195])
average_speed = np.mean(motor_speed)
print("average speed :",(average_speed))

model_accuracy = np.array([92.5, 93.1, 91.8, 94.0])
median_accuracy =np.median(model_accuracy)
print("median of all : ",(median_accuracy))

btc_price = np.array([118500, 118700, 118300, 118900])
print("standard deviation :",np.std(btc_price))

sensor_values = np.array([0.25, 0.28, 0.26, 0.27])
print("maximum value :",np.max(sensor_values) )

#code 1
"""
#Step 1 — Array Indexing
import numpy as np 
marks = np.array ([85,92,35,88,95])
print ("Marks :",marks)

print("first student :",marks[0])
print("second student :",marks[1])
print("last student:",marks[-1])

#Step 2 — Array Slicing

print("First three :",marks[:3])
print("Last two :",marks[-2:])
print("Middle:",marks[1:4])
print("Steps :",marks[0:5:2])

#Step 3 — Update Values

marks[2] = 40
print ("Updated Marks :",marks)

#Step 4 — Useful NumPy Functions

print("Maximum :",np.max(marks))
print("Minimum :",np.min(marks))
print("Sum :",np.sum(marks))
print("Average :",np.mean(marks))

"""
# code 2 - Mini Challenge :

import numpy as np
attendance = np.array([95,87,100,76,92])

print("all attendance :",attendance)

print("Highest Attendance :",np.max(attendance))
print("Lowest Attendance :",np.min(attendance))
print("Sum of all Attendance :",np.sum(attendance))
print("Average Attendance :",np.mean(attendance))
print(f"Average Attendance : {np.mean(attendance):.2f}") #You'll use formatting like :.2f a lot when displaying percentages, ML model accuracy, and financial values.

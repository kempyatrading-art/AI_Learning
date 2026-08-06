#code :1
"""
# Step 1 — Matrix Addition :
import numpy as np  
matrix_a = np.array([
    [10,20],
    [30,40]
])

matrix_b = np.array([
    [5,10],
    [15,20]
])

#result = matrix_a + matrix_b

result = np.add(matrix_a,matrix_b)

print("="*15)
print("Matrix Addition")
print("="*15)

print("\nmatrix_A :")
print(matrix_a)

print("\nmatrix_B :")
print(matrix_b)

print("\nAddition :\n",result)

"""
# Mini Challenge 1 :- code 2
"""
import numpy as np 
robot_line_1 = np.array([
    [120,130],
    [120,128]
])

robot_line_2 = np.array([
    [15,20],
    [18,22]
])

Total_Production = np.add(robot_line_1,robot_line_2)

print("="*30)
print("Robot Total Production")
print("="*30)

print("\nRobot line 1:\n",robot_line_1)
print("Robot line 2:\n",robot_line_2)

print("\nTotal Production :\n",Total_Production)

"""
# Mini Challenge 1 improvement :- code 3
"""
import numpy as np 
robot_line_1 = np.array([
    [120,130],
    [120,128]
])

robot_line_2 = np.array([
    [15,20],
    [18,22]
])

Total_Production = np.add(robot_line_1,robot_line_2)

print("="*30)
print("Robot Total Production")
print("="*30)

print("\nRobot Line 1")
print(robot_line_1)

print("\nRobot Line 2")
print(robot_line_2)

print("\nTotal Production")
print(Total_Production)
"""

# Step 2 — Matrix Subtraction : - code 4
"""
import numpy as np 
robot_line_1 = np.array([
    [120, 130],
    [120, 128]
])

robot_line_2 = np.array([
    [15, 20],
    [18, 22]
])

difference = robot_line_1 - robot_line_2

print("="*30)
print("Robot Total Production")
print("="*30)

print("\nRobot Line 1")
print(robot_line_1)

print("\nRobot Line 2")
print(robot_line_2)

print("\nMatrix Subtraction :")
print(difference)

"""
# Step 3 — Matrix Multiplication :-  code 5
"""
#Element-wise Multiplication (* or np.multiply): Multiplies matching elements at identical positions.
#Dot Product / Matrix Multiplication (@ or np.dot): Standard linear algebra matrix multiplication (row * column dot products).

import numpy as np 
matrix_a = np.array ([
    [1,2],
    [3,4]
])

matrix_b = np.array([
    [5,6],
    [7,8]
]) 

# 1. Element-wise Multiplication
element_wise = matrix_a * matrix_b

# 2. True Matrix Multiplication (Dot Product)
matrix_multiplied = matrix_a @ matrix_b

print("="*30)
print("Matrix Multiplication")
print("="*30)

print("\nMatrix A")
print(matrix_a)

print("\nMatrix B")
print(matrix_b)

print("\nElement-wise Product (*):")
print(element_wise)

print("\nDot Product / Matrix Multiplication (@):")
print(matrix_multiplied)

"""

# Step 4 — Matrix Transpose :- code 6 

# Step 4 — Matrix Transpose :- 
# A transpose flips a matrix over its diagonal—switching its rows and columns. In NumPy, you simply use .T on any array.
"""
import numpy  as np 

# Sample robot sensor data (3 robots x 3 parameters)
robot_data = np.array([
    [101,92,45],
    [102,87,48],
    [103,95,43]
])

#transposed_data = np.transpose(robot_data)
transposed_data = robot_data.T

print("="*35)
print("MATRIX TRANSPOSE")
print("="*35)

print("\nOriginal Matrix (Rows = Robots, Cols = Features):")
print(robot_data)

print("\nTransposed Matrix (Rows = Features, Cols = Robots):")
print(transposed_data)

"""
# Step 5 — Identity Matrix & Challenge :- code 7 

#What is an Identity Matrix? :- An identity matrix is a square matrix where:
#All diagonal elements = 1
#All other elements = 0
#Example:
#[1 0 0]
#[0 1 0]
#[0 0 1]

import numpy as np 

# 1. Creating Identity Matrices
identity_3 = np.eye(3)
identity_4 = np.eye(4)

print("="*35)
print("IDENTITY MATRIX")
print("="*35)

print("\n3 * 3 Identity Matrix :")
print(identity_3)

print("\n4 * 4 Identity Matrix :")
print(identity_4)

# 2. Industrial Challenge: Robot Position Transformation
robot_position = np.array([
    [100], # X coordinate
    [50], # Y coordinate
    [20] # Z coordinate 
])

# Multiply position vector by Identity matrix
new_position_a = identity_3 @ robot_position
new_position_b = identity_3 * robot_position

print("\n" + "="*35)
print("INDUSTRIAL CHALLENGE")
print("="*35)

print("\nOriginal Robot Position :")
print(robot_position)

print("\nNew Robot Position (after Identity @ Position ):")
print(new_position_a)

print("\nNew Robot Position (after Identity * Position ):")
print(new_position_b)



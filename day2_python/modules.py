"""
Program 1 — What is a Module?

A module is simply a Python file that contains code.

For example:

math.py
random.py
json.py

are all modules.
"""
# Program 2 — Import the math Module
"""
import math

print(math.sqrt(25))
print(math.sqrt(64))
print(math.pi)

"""
# Program 3 — More Math Functions
"""
import math

print(math.pow(2,5))
print(math.factorial(5))
print(math.ceil(5.2))
print(math.floor(5.9))
"""
# Mini Challenge 1

import math

# 1. Ask the user for a number
user_input = input("Enter a number : ")

# 2. Convert the input to a float so it can handle decimals too

number = float(user_input)
    
# 3. Calculate the values
sq_root = math.sqrt(number)
square = number ** 2
cube = number ** 3

# 4. Print the results clearly

print (f"square Root : {sq_root}")
print (f"Square      : {square}")
print (f"Cube        :{cube}")
    

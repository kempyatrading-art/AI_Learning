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
    
"""

# random Module 🎲
"""
import random
number = random.randint(1,10)
print(number)

"""
# Mini Challenge 2
"""
import random
while True : 
    
    number = random.randint(1,6)
    user_guesses = int(input("guesses the number and enter the number :" ))
    if number == user_guesses  :
        print ("correct")
        print (f"the correct number was : {number}")
        break
    else :

        print ("wrong! guesses")
        print (f"the correct number was :{number}")
                
"""

"""
# Mini Challenge 3
import random
number = random.randint(1,6)
while True : 
    user_guesses = int(input("guesses the number and enter the number :" ))
    if number == user_guesses  :
        print ("🎉 Correct!")
        print (f"the correct number was : {number}")
        break
    else :
        if user_guesses > number:
            print ("📈 Too high! Try a smaller number.")
            print ("wrong! guesses")
        elif user_guesses < number :
            print ("📉 Too low! Try a bigger number.")
            print ("wrong! guesses")
            
"""
"""
# Mini Challenge 4
import random
number = random.randint(1,6)
attempts =5
while attempts >0:
    
    user_guesses = int(input("guesses the number and enter the number :" ))
    if number == user_guesses  :
        print ("🎉 Correct!")
        print (f"the correct number was : {number}")
            
        break
    else :
        attempts -=1
        if attempts == 0:
            print("\n💀 Game Over!")
            print(f"The correct number was: {number}")
            break
        if user_guesses > number:
            print (f"Attempts left: {attempts}")
            print ("📈 Too high! Try a smaller number.")
            print ("❌ wrong! guesses")
        elif user_guesses < number :
            print (f"Attempts left: {attempts}")
            print ("📉 Too low! Try a bigger number.")
            print ("❌ wrong! guesses")
            
"""
from calculator import add, multiply

a = float(input("Enter value for (a): "))
b = float(input("Enter value for (b): "))

print(f"Add of a+b : {add(a, b)}")
print(f"Multiply of a*b : {multiply(a, b)}")
"""
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
print("Addition: ", a+b)
print("Multiplication: ", a*b)
try :
    if b != 0 :
        print("Division: ", a/b)
        print("modulus: ", a%b)

except ZeroDivisionError :
    print("❌ Division by zero is not allowed.")
    print("square: ", a**2,b**2)
    
"""
"""
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

print("Addition: ", a+b)
print("Multiplication: ", a*b)

if b != 0 :
    print("Division: ", a/b)
    print("modulus: ", a%b)
else :
    print("❌ Division by zero is not allowed.")
    
print("square: ", a**2,b**2)
"""

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", a + b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
        print("Modulus:", a % b)
    else:
        print("❌ Division by zero is not allowed.")

    print(f"Square of A: {a**2}")
    print(f"Square of B: {b**2}")

except ValueError:
    print("❌ Please enter valid numbers.")
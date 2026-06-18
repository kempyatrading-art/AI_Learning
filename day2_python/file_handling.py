#Program 1 - Write to a File
"""
with open ("student.txt","w") as file:
    file.write("Rahul\n")
    file.write("Robotics and Automation\n")
    file.write("AI engineer\n")
print ("Data Saved Successfully")
"""

#Program 2 - Read a File
"""
with open ("student.txt","r") as file :
    data=file.read()
print(data)    
"""
#Program 3 - Append Data
"""
with open ("student.txt","a") as file :
    file.write ("Python Developer\n")
print("new data added ")
"""
##Program 3.1 - Append Data and print updated data

"""
with open ("student.txt","a") as file :
    file.write ("Python Developer\n")
print("new data added ")

with open ("student.txt","r") as file :
    data=file.read()
print (data)
"""
#Program 4 - Store Your Information
"""
name = input("Enter the Name :")
usn = input("Enter the USN :").upper()
branch = input("Enter the Branch :")
goal = input("Enter the Goal :")

with open ("profile.txt","w") as file :
    file.write (f"Name : {name}\n")
    file.write (f"USN : {usn}\n")
    file.write (f"Branch : {branch}\n")
    file.write (f"Goal : {goal}\n")
    
    print ("profile saved ")
    """
#Mini Project

"""
usn =input("Enter the USN :")
name =input("Enter the Name :")
cgpa =input("Enter the CGPA :")

with open ("students.txt","w") as file :
    file.write (f"{usn.upper()}\n{name}\n{cgpa}\n")
    print("student Record Saved")
"""
#Mini Project 2.0
usn =input("Enter the USN :")
name =input("Enter the Name :")
cgpa =input("Enter the CGPA :")

with open ("students.txt","a") as file :
    file.write("\n")
    file.write (f"USN :{usn.upper()}\n")
    file.write (f"Name :{name}\n")          
    file.write (f"CGPA :{cgpa}\n")
    file.write("--------------------\n")
print("student Record Saved")
#Step 2 — Create Your First JSON Program 

"""
import json

student ={
    "name": "Rahul",
    "branch" : "Robotics and Automation",
    "cgpa" : 8.18,
    "skills" : ["Python" , "AI" ,"Robotics"]
}
print(student)

"""
# Step 3 — Save Dictionary to JSON File
"""
import json
student = {
    "name" : "Rahul",
    "branch" : "Robotics and Automation",
    "cgpa" : 8.18,
    "skills" : ["Python" , "AI" , "Robotics"]
}

with open ("student.json","w") as file :
    json.dump(student, file, indent=4)
print("json file saved successfully") 

"""

# Step 4 — Read JSON File
"""
import json
student = {
    "name" : "Rahul",
    "branch" : "Robotics and Automation",
    "cgpa" : 8.18 ,
    "skills" : ["Python" , "AI" , "Robotics"]
}

with open ("student.json","r") as file :
    data = json.load(file)
print (data)
"""

# Step 5 — Access Data

"""
import json

student = {
    "name" : "Rahul",
    "branch" : "Robotics and Automation",
    "cgpa" : 8.18 ,
    "skills" : ["Python" , "AI" , "Robotics"]
}

with open ("student.json","r") as file :
    data = json.load(file)
print (data)
print(data["name"])
print(data["branch"])
print(data["cgpa"])
print(data["skills"])
"""
# Mini Project
"""
import json

student = {
    "usn" : "2VX23RA406",
    "name" : "Rahul",
    "branch" : "Robotics and Automation",
    "cgpa" : 8.18 ,
    "goal" : "AI Engineer"
}

with open ("student.json","w") as file :   #replace "a" for add data same file , "w" for rewrite everything after cleaning , "r"  for reading data from file 
    #file.write("\n")    # create new empty line for lock cleaner data while adding data  again and again . create blank space i between 
    #file.write("\n")
    json.dump(student, file, indent=4)
    
print ("Student JSON Saved")

with open ("student.json","r") as file :
    data = json.load(file)
    
print ("USN :", data ["usn"])
print ("Name :", data ["name"])
print ("Branch :", data ["branch"])
print ("CGPA :", data ["cgpa"])
print ("Goal :", data ["goal"])

"""

# Mini Project : Next Level: Multiple Students JSON Database
"""
import json 
# 1. Define a database structure with a list of multiple students
students = {
    "students": [
        {
            "usn": "2VX23RA406",
            "name": "Rahul",
            "branch": "Robotics and Automation",
            "cgpa": 8.18,
            "goal": "AI Engineer"
        },
        {
            "usn": "2VX23RA404",
            "name": "Raghav",
            "branch": "Robotics and Automation",
            "cgpa": 8.20,
            "goal": "Robotics Engineer"
        },
        {
            "usn": "2VX23RA405",
            "name": "Raghu",
            "branch": "Mechanical Engineering",
            "cgpa": 8.50,
            "goal": "Automation Specialist"
        }
    ]
}
# 2. Write the entire database to a new file 'students.json'
with open ("students.json","w") as file :
    json.dump(students,file,indent=4)
    
print("Students Database Saved Successfully!\n")

# 2. Write the entire database to a new file 'students.json'
with open ("students.json","r") as file :
    data = json.load (file)
    
# 4. Loop through the list of students
print ("----FETCHING STUDENT PROFILES---")

for student in data ["students"] :
    print ("USN    :",student ["usn"])
    print ("NAME   :",student ["name"])
    print ("BRANCH :",student ["branch"])
    print ("CGPA   :",student ["cgpa"])
    print ("GOAL   :",student ["goal"])
    print ("-" *30) #separate line
"""
# Mini Project : Instead of printing every student, ask the user for a USN.
import json
with open ("students.json","r") as file :
    data = json.load(file)
    
print ("--- STUDENT DATABASE SEARCH SYSTEM ---")
while True :
    
    search_usn = input ("Enter the USN :").upper()
    found = False 

    for student in data ["students"] :
        if student["usn"] == search_usn :
            print ("\n student profile found :")
            print ("-" * 30)
            print ("USN    :",student ["usn"])
            print ("NAME   :",student ["name"])
            print ("BRANCH :",student ["branch"])
            print ("CGPA   :",student ["cgpa"])
            print ("GOAL   :",student ["goal"])
            print ("-" *30) #separate line
            
            found = True
            
            break
    if not found :
            print (f"\n no student found with this USN : {search_usn}") 
            
    while True:

            choice = input("\nDo you want to search again? (Y/N): ").upper()

            if choice == "Y":
                break          # leave this small loop and search again

            elif choice == "N":
                print("Thank you for using Student Database.")
                exit()         # end the program

            else:
                print("Invalid choice. Please enter only Y or N.")
            
            
            
            
            
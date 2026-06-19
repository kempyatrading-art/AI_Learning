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

import json

"""
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
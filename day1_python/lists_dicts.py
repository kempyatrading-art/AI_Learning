#lists_dicts.py:
"""

#part 1 lists :
models =["GPT","CLAUDE","GEMINI"]
print (models)

#Access Individual items

print (models[0])
print (models[1])
print (models[2])

# Adding a new item to the end of the list

models .append ("DeepSeek")
print (models[3])
print ("updated list :",models)

"""
#Part 2 — Dictionaries :
"""
student = {
    "name": "Rahul",
    "branch": "Robotics and Automation",
    "goal": "AI Engineer"
}

#Print Values
print (student["name"])
print (student["branch"])
print (student["goal"])

# Adding a brand new Key-Value pair

student["cgpa"] = 8.18
print (student["cgpa"])
print (student )

""" 
students = [
    {
        "name": "Rahul",
        "goal" : "AI Engineer"
    },
    {
        "name": "Raghav",
        "goal": "AI Engineer"
    }
]
#now print :
for student in students :
    print("NAME :",student["name"])
    print("GOAL :",student["goal"])
    

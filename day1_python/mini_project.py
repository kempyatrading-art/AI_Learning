students = {
    "2VX23RA406" :{
        "name" : "Rahul",
        "branch": "Robotics and Automation",
        "goal" : "AI Engineer",
        "cgpa" : "8.18",
        "skills" : ["Python","AI","Trading","Robotics"]
    },
    
    "2VX23RA404":{
        "name" : "Raghav",
        "branch": "Robotics and Automation",
        "goal" : "AI Engineer",
        "cgpa" : "8.180",
        "skills" : ["Python","AI","Robotics"]
    },
    "2VX23RA405":{
        "name": "Raghu",
        "branch": "Robotics and Automation",
        "goal": "Hardware Engineer",
        "cgpa": "8.5",
        "skills":["ROS","C++","Arduino"]
    }
}

def search_student ():
    attempts =3
    while attempts >0:
        usn = input("Enter USN :").upper()
        if usn in students :
            
            student = students[usn]
            print ("\nstudent found")
            print("Name :",student["name"])
            print("Branch :",student["branch"])
            print("Goal :",student["goal"])
            print("CGPA :",student["cgpa"])
            print("Skills :", ", ".join(student["skills"]))
            
            return
        else :
            attempts -= 1
            print ("usn not found chuck your usn  and try again")
            print("attempts left :",[attempts])
            print("\nacces block")
            
while True:
    search_student()
    
    again = input("\nDo you want to search again? (Y/N) : ").upper()
    if again !="Y":
        print("Goodbye!")
        break


            
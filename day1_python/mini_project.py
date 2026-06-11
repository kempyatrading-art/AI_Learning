students = {
    "2VX23RA406" :{
        "name" : "Rahul",
        "branch": "Robotics and Automation",
        "goal" : "AI Engineer"
    },
    
    "2VX23RA404":{
        "name" : "Raghav",
        "branch": "Robotics and Automation",
        "goal" : "AI Engineer"
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
            
            return
        else :
            attempts -= 1
            print ("usn not found chuck your usn  and try again")
            print("attempts left :",[attempts])
            print("\nacces block")
search_student()
            
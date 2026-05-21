students = {
    "2VX23RA406": {
        "name": "Rahul",
        "branch": "Robotics and Automation",
        "dob": "24-07-2002",
        "goal": "AI Engineer"
        },
    "2VX23RA404": {
        "name": "Raghav",
        "branch": "Robotics and Automation",
        "dob": "16-10-2003",
        "goal": "Trader"
    }
    
}

usn = input ("Enter your USN : ")
if usn in students:
    student = students[usn]
    print("\nstudent found")
    print ("Name : ", student["name"])
    print ("Branch : ", student["branch"])
    print ("Date of Birth : ", student["dob"])
    print ("Goal : ", student["goal"])
    
else :
    print ("Enterd USN not Found in Database ")

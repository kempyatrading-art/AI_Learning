import json

age = int(input("please tell your age :"))

if age >= 18 :
    
    print("✅ You are eligible to vote ")
    
    vote = input("Enter your USN: ").upper()
    
    with open ("student_vote.json","r") as file :
        data =json.load(file)
        
    if vote in data:
        print ("❌ Your vote is already present in our database ")
        print("You cannot vote again.")
        
    else :
        
        data.append(vote)    
            
        
    with open ("student_vote.json","w") as file :
        json.dump(data ,file ,indent=4)
        
    print("✅ Thank you for voting!")
            
else :
    
    print("❌ You are not eligible to vote.")


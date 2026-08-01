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
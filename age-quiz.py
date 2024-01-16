#************pseudo code**********
#The program will take the age as input from the user and than the entered age will compared to different age groups
#The program will use if elif control structure to caompare the different entries
#if the age matched with condtion given in if or elif body , only the specific block will execute and rest of the blocks will skipped




#Take age from the user as integer
age=int(input("Please enter the age"))
#Compare if age is less than 100 go to if body 
if (age < 100):
    #Compare if age greater or equal to 65 print some message
    if(age >= 65):
        #Print message
        print("Enjoy your retirement :)")
        #Compare if age greater or equal to 40 than go to condition body and print message
    elif (age >= 40):
          print("You are over the hill.")
          # Compare if age is equal to 21 than go to elif body and print message
    elif (age == 21):
        print("Congrats on your 21st!")
        #Compare if age is less than 13 than go to elif body and print message
    elif (age < 13):
        print("You qualify for the kiddie discount")
        #End of nested if , if no condition true print the statement in else body
    else:
        print("Age is but a number")
# If user input is over 100 print the message in outer else body

else:
    print("Sorry you are dead")
    
    
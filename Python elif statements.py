Grade1 = int(input("Put in your first grade. "))
Grade2 = int(input("Put in your second grade. "))
Grade3 = int(input ("Finally, put in your third grade. " ))

avg = (Grade1 + Grade2 + Grade3)/3

#elif is an if conditon nested in a if statement
if(avg >= 90)and(avg <=100): # "and" responds if both conditions are met
    print("You got an A with an average score of " + str(avg)) #str turns "avg" into a string
elif(avg >=80) and (avg <=89):
    print("You got a B with an average score of " + str(avg))
elif(avg >= 0) and (avg <=79):
    print("You got a grade below a B with an average score of " + str(avg))
elif(avg >0) or (avg > 100): # "or" responsed to either condition
    print("Invalid input(s), please renter your grades in proper format")
        
        
    

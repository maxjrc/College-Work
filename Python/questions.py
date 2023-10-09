def feedback():
    feedbacki = input("Did I get the person you are thinking of? ")
    if feedbacki == "Y":
        print("Thanks for your feedback! Glad we could guess the person you were thinking of!")
    if feedbacki == "N":
        print("Sorry we couldn't get the person you were thinking of! ")
        

q1 = input("Is your person from a TV Show? Y/N ")
if q1 == "Y":
    q2 = input("Is your charecter tall? Y/N ")
    if q2 == "N":
        q3 = input("Is your person a girl? ")
        if q3 == "N":
            q4 = input("Are they indian? ")
            if q4 == "Y":
                print("The person you are thinking of is raji from Big Bang Theory!")
                feedback()
            else:
                print("Not a valid input!")
            if q4 == "N":
                q5 = input("Did they have mother that always use to shout?")
                if q5 == "Y":   
                    print("The person you are thinking of is Howard!")
                    feedback()
                else:
                    print("Not a valid inpuT!")
            else:
                print("Not a valid input!")
        else:
            print("Not a valid input!")
        if q3 == "Y":
         q4 = input("Are they known as the 'mother' of sheldon? " )
        else:
            print("Invalid Input.")
        if q4 == "Y":
                print("Your charector is Penny from Big Bang Theory!")
                feedback()
        if q4 == "N":
            print("You got me!")
            feedback()
        else:
            print("Not a valid input!")
    else:
        print("Not a valid input!")

    if q2 == "Y":
        q3 = input("Does your charecter have a specific place on there couch? Y/N ")
        if q3 == "Y":
            print("The person your thinking of is Sheldon Cooper from Big Bang Theory!")
            feedback()
if q1 == "N":
    print("You got me! I can't think of the person you were thinking of!")
    feedback()

else:
    print("Not a valid input!")




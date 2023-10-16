def start():
    print("Welcome to the Dino Guesser!")
    startt = input("Would you like to begin? Y/N ")
    q1 = ""
    q2 = ""
    startt = ""
    q3 = ""
    
    if startt == "Y":
        begintree()
    if startt == "N":
        stopplaying()
    else:
        print("Not a valid option!")

def begintree():
    print("Let's begin!")
    q1 = input("Does your dino eat meat? ")
    if q1 == "Y":
        q2 = input("Does it have short arms? ")
        if q2 == "Y":
            print("It's a T-Rex! I got it! ")
            stopplaying()
        if q2 == "N":
            q3 = input("Does it have a big footprint? ")
            if q3 == "N":
                print("Xuanhanosaurus I say!")
                stopplaying()
            if q3 == "Y":
                print("It's a Pachycephalosaurus")
                stopplaying()
    if q1 == "N":
        print("I got it! It's a sauropodomorphs!")
        stopplaying()
def stopplaying():
    print("Thanks for playing!")

start()
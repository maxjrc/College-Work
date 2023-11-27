

def login():
    username = "Max"
    password = "Password123"
    iusername = input("Please enter a username: ")
    if iusername == username:
        ipassword = input("Please enter the password: ")
        if ipassword == password:
            menu()
        else:
            print("Incorrect Password")
            login()
    else:
        print("Invalid Username")
        login()


def menu():
    print("Welcome!")
    ichoice = input("Please enter Chess, Billards, Darts: ")
    if ichoice == "Chess":
        print("You selected chess!")
    elif ichoice == "Billards":
        print("You have selected billards!")
    elif ichoice == "Darts":
        print("You have selected darts: ")
    else:
        print("Not a valid choice!")
        menu()


login()

def menu():
    op = input("Please enter: ")
    if op == "1":
        read()
    if op == "2":
        search()
    else:
        print("Not a valid option!")

def read():
    file = open("gamerscore.csv", "r")
    line = file.readline()

    while(line):
        print(line)
        line=file.readline()
    file.close()

def search():
    file = open("gamerscore.csv", "r")
    line = file.readline()
    SearchFind = input("Please enter the name you wish to find: ")
    while(line):
        data = line.split(",")
        if data[0]==SearchFind:
                print("Handle: ", data[0])
                print("Gamerscore: ", data[1])
        
        else:
            print("Not found!")
        
        line=file.readline()
    file.close()


def edit():
    file = open("gamerscore.csv", "r")
    line = file.readline()
    EditInput = input("Please enter the name you wish to edit: ")
    



menu()
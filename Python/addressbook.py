global excelbook
excelbook = "Book1.csv"

def menu():
    op = input("Please enter an option: ")
    if op == "1":
        find()
    if op == "2":
         changebook()
def find():
    file = open("Book1.csv", "r")
    line = file.readline()
    SearchFind = input("Please enter the name you wish to find: ")
    while(line):
        data = line.split(",")
        if data[0]==SearchFind:
                print("Name: ", data[0])
                print("Address: ", data[1])
                print("City: ", data[2])
                print("Phone Number: ", data[3])
                break
        else:
            print("Not found!")
        
        line=file.readline()
    file.close()

def editbook():
    file = open("Book1.csv", "w")
    line = file.readline()
    EditInput = input("Please enter the name you wish to edit: ")
    


def changebook():
     change = input("Please enter the book you would like to use: ")
     excelbook = change + ".csv"
     print("Changed!")
     menu()
menu()
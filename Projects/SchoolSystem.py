# Group Tutor Project by Max Croft

import sqlite3
import random

conn = sqlite3.connect("student.db")
curr = conn.cursor()


def menu(user):
    print("Welcome " + user[1] + " to Tree Road School." + " Please select an option below.")
    print("1. View Student Details")
    print("2. Add Student")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Generate Report")
    choice = input("Choice: ")
    if choice == "1":
        viewstudentdetails(user)
    elif choice == "2":
        createstudent(user)
    elif choice == "3":
        editstudent(user)
    elif choice == "4":
        deletestudent(user)
    elif choice == "5":
        generatereport(user)
    else:
        print("Invalid Choice. Please try again")
        menu(user)

def login():
    print("Welcome to the School System")
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    curr.execute("SELECT * FROM Staff WHERE username = ? AND password = ?", (username, password))
    rows = curr.fetchall()
    if len(rows) == 0:  # Check if rows list is empty
        print("No Login Found. Please try again")
        login()
    else:  
        if username == rows[0][3] and password == rows[0][4]:
            print("Login Successful")
            user = rows[0]
            menu(user)
        else:
            print("Login Failed. Please try again")
            login()

def createstafflogin():
    print("Create Staff Login")
    print("Please enter your details below")
    firstname = input("First Name: ")
    surname = input("Surname: ")
    username = input("Username: ")
    password = input("Password: ")
    staffid = str(random.randint(1000, 9999))
    curr.execute("INSERT INTO Staff (StaffID, FirstName, LastName, Username, Password) VALUES (?, ?, ?, ?, ?)", (staffid, firstname, surname, username, password))
    conn.commit()
    print("Login Created Successfully")


def createstudent(user):
    print("Create A Student")
    print("Please enter the student details below: ")
    firstname = input("First Name: ")
    surname = input("Surname: ")
    age = input("Date of Birth: ")
    home_address = input("Home Address: ")
    home_phone_number = input("Home Phone Number: ")
    gender = input("Gender: ")
    studentid = str(random.randint(1000, 9999))
    tutor_group = input("Tutor Group: ")
    curr.execute("INSERT INTO Students (student_id, surname, date_of_birth, home_address, home_phone_number, gender, tutor_group) VALUES (?, ?, ?, ?, ?, ?, ?)", (studentid, firstname, surname, age, home_address, home_phone_number, gender, tutor_group))   
    conn.commit()
    print("Student Created Successfully")
    
login()
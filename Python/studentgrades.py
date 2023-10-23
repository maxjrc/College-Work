import sqlite3
from datetime import date
conn = sqlite3.connect("studentdata.db")
curr = conn.cursor()


def menu():
    print("Welcome to the Grading System!")
    op = input("Please select an option: 1. Review Grades 2. Find Student 3. Add Grades ")
    if op == "1":
        reviewgrades()
    if op == "2":
        print("Not ready!")
    if op == "3":
        addtest()
    else:
        print("Not a valid option.")
        menu()


def reviewgrades():
    student = input("What student do you want to review? ")
    # get the test from the database
    conn.execute("SELECT * FROM tests WHERE student_name = ?", (student,))
    rows = curr.fetchall()
    print(rows)
    for row in rows:
        print(row)
    menu()

def addtest():
    nametest = input("Please enter the name of the test? ")
    tutorname = input("Please enter the name of the marker? ")
    testdate = date.today()
    students = int(input("How many students tests did you mark? "))
    for x in range(students):
        studentname = input("Please enter the name of the student? ")
        studentgrade = input("Please enter the score of the student? ")
        conn.execute("INSERT INTO tests (test_name, tutor_name, test_date, student_name, score) VALUES (?, ?, ?, ?, ?)", (nametest, tutorname, testdate, studentname, studentgrade))
        conn.commit()
        
    print("Added the test and all grades.")
    menu()
menu()
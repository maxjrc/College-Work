import sqlite3
from datetime import date
conn = sqlite3.connect("studentdata.db")
curr = conn.cursor()

def menu():
    while True:
        print("=====================================")
        print("Welcome to the Grading System!")
        op = input("Please select an option: 1. Review Grades 2. Find Student 3. Add Grades 4. Delete Grades 5. Change Grades 6. Generate Report ")
        if op == "1":
            reviewgrades()
        elif op == "2":
            findstudent()
        elif op == "3":
            addtest()
        elif op == "4":
            deletetest()
        elif op == "5":
            changegrade()
        elif op == "6":
            generatereportcard()
        else:
            print("Not a valid option.")

def reviewgrades():
    test = input("What test do you want to review? ")
    curr.execute("SELECT * FROM tests WHERE test_name = ?", (test,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No tests found.")
        return
    for row in rows:
        print("=====================================")
        print("Test Name: ", row[3])
        print("Student Name: ", row[0])
        print("Student Grade: ", scorechanger(row[2]))
        print("Test Date: ", row[1])
        print("Marked by: ", row[4])
        print("=====================================")
    conn.commit()

def addtest():
    nametest = input("Please enter the name of the test? ")
    curr.execute("SELECT * FROM tests WHERE test_name = ?", (nametest,))
    rows = curr.fetchall()
    if len(rows) > 0:
        print("Test already exists.")
        return
    tutorname = input("Please enter the name of the marker? ")
    testdate = date.today()
    students = int(input("How many students tests did you mark? "))
    for x in range(students):
        studentname = input("Please enter the name of the student? ")
        studentgrade = input("Please enter the score of the student? ")
        conn.execute("INSERT INTO tests (test_name, tutor_name, test_date, student_name, score) VALUES (?, ?, ?, ?, ?)", (nametest, tutorname, testdate, studentname, studentgrade))
        conn.commit()
        
    print("Added the test and all grades.")


def deletetest():
    student = input("What student do you want to delete? ")
    curr.execute("DELETE FROM tests WHERE student_name = ?", (student,))
    conn.commit()
    print("Deleted the test and all grades.")

def changegrade():
    student = input("What student do you want to change? ")
    conn.execute("SELECT * FROM tests WHERE student_name = ?", (student,))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    test = input("What test do you want to change? ")
    newgrade = input("What is the new grade? ")
    conn.execute("UPDATE tests SET score = ? WHERE student_name = ? AND test_name = ?", (newgrade, student, test))
    conn.commit()
    print("Changed the grade.")

def findstudent():
    student = input("What student do you want to find? ")
    curr.execute("SELECT * FROM tests WHERE student_name = ?", (student,))
    rows = curr.fetchall()
    for row in rows:
        print("=====================================")
        print("Test Name: ", row[3])
        print("Score: ", row[2])
        print("Grade: ", scorechanger(row[2]))
        print("Test Date: ", row[1])
        print("Marked by: ", row[4])
        print("=====================================")


def scorechanger(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def generatereportcard():
    student = input("What student do you want to generate a report card for? ")
    curr.execute("SELECT * FROM tests WHERE student_name = ?", (student,))
    rows = curr.fetchall()
    # create a text file with the student name
    file = open(student + ".txt", "w")
    file.write("Report Card\n")
    file.write("Student Name: " + student + "\n")
    total = 0
    for row in rows:
        total += row[2]
        average = total / len(rows)
        average = scorechanger(average)
        message = checkifgraduate(average)
    file.write("Year Grade: " + average + "\n")
    file.write("=====================================\n")
    file.write("Test Results\n")
    for row in rows:
        file.write("Test Name: " + row[3] + "\n")
        file.write("Grade: " + scorechanger(row[2]) + "\n")
        file.write("=====================================\n")
    file.write(message)
    file.close()
    print("Generated the report card.")

def checkifgraduate(average):
    if average == "A":
        return "You have graduated congratulations and we wish you the best of luck in your future endeavors."
    elif average == "B":
        return "You have graduated congratulations and we wish you the best of luck in your future endeavors."
    elif average == "C":
        return "You have graduated congratulations and we wish you the best of luck in your future endeavors."
    elif average == "D":
        return "You have graduated congratulations and we wish you the best of luck in your future endeavors."
    else:
        return "Unfortunately you have not graduated, we have sent you a letter with more information about the next steps you can take to graduate. You may appeal your marks by contacting your tutor."
menu()
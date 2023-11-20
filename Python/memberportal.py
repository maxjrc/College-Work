import sqlite3
import time
import random
conn = sqlite3.connect("memberdata.db")
curr = conn.cursor()



# commit the changes
conn.commit()
def menu(row):
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Member")
    print("4. View Member")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_member(row)
    elif choice == "2":
        remove_member(row)
    elif choice == "3":
        update_member(row)
    elif choice == "4":
        view_member(row)
    elif choice == "5":
        login()
    else:
        print("Invalid choice")
        menu(row)


def add_member(row):
    print("Add Member")
    membership_id = "Rock_" + str(random.randint(1000, 9999))  
    name = input("Name: ")
    email = input("Email: ")
    gender = input("Gender: ")
    dob = input("Date of Birth: ")
    skill_level = input("Skill Level: ")
    plan = input("Plan: ")
    date = time.strftime("%d/%m/%Y")
    end_date = input("End Date: ")
    payment_status = input("Payment Status: ")
    membership_status = "Active"
    curr.execute("INSERT INTO Membership VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (membership_id, name , email, dob, gender, skill_level, plan, date, end_date, payment_status, membership_status))
    conn.commit()
    print("Member added successfully")
    menu(row)

def remove_member(row):
    print("Remove Member")
    membership_id = input("Membership ID: ")
    curr.execute("SELECT * FROM Membership WHERE membership_id=?", (membership_id,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("Membership ID does not exist")
        remove_member(row)
    else:
        choice = input("Are you sure you want to remove this member: " + str(rows[0][1]))
        if choice == "yes":
            curr.execute("DELETE FROM Membership WHERE membership_id=?", (membership_id,))
            conn.commit()
            print("Member removed successfully")
            menu(row)
        else:
            print("Member not removed")
            menu(row)

def update_member(row):
    print("Updating a member")
    membership_id = input("Membership ID: ")
    curr.execute("SELECT * FROM Membership WHERE membership_id=?", (membership_id,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("Membership ID does not exist")
        update_member(row)
    else:
        print("Please say what you would like to update")
        print("1. Name")
        print("2. Email")
        print("3. Gender")
        print("4. Skill Level")
        print("5. Plan")
        print("6. End Date")
        print("7. Payment Status")
        print("8. Membership Status")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Name: ")
            curr.execute("UPDATE Membership SET name=? WHERE membership_id=?", (name, membership_id))
            conn.commit()
            print("Name updated successfully")
            menu(row)
        elif choice == "2":
            email = input("Email: ")
            curr.execute("UPDATE Membership SET email=? WHERE membership_id=?", (email, membership_id))
            conn.commit()
            print("Email updated successfully")
            menu(row)
        elif choice == "3":
            gender = input("Gender: ")
            curr.execute("UPDATE Membership SET gender=? WHERE membership_id=?", (gender, membership_id))
            conn.commit()
            print("Gender updated.")
            menu(row)
        elif choice == "4":
            skill_level = input("Skill Level: ")
            curr.execute("UPDATE Membership SET skill_level=? WHERE membership_id=?", (skill_level, membership_id))
            conn.commit()
            print("Skill Level updated.")
            menu(row)
        elif choice == "5":
            plan = input("Plan: ")
            curr.execute("UPDATE Membership SET membership_plan=? WHERE membership_id=?", (plan, membership_id))
            conn.commit()
            print("Plan updated.")
            menu(row)
        elif choice == "6":
            end_date = input("End Date: ")
            curr.execute("UPDATE Membership SET end_date=? WHERE membership_id=?", (end_date, membership_id))
            conn.commit()
            print("End Date updated.")
            menu(row)
        elif choice == "7":
            payment_status = input("Payment Status: ")
            curr.execute("UPDATE Membership SET payment_status=? WHERE membership_id=?", (payment_status, membership_id))
            conn.commit()
            print("Payment Status updated.")
            menu(row)
        elif choice == "8":
            membership_status = input("Membership Status: ")
            curr.execute("UPDATE Membership SET membership_status=? WHERE membership_id=?", (membership_status, membership_id))
            conn.commit()
            print("Membership Status updated.")
            menu(row)
        else:
            print("Invalid choice")
            update_member(row)


def view_member(row):
    id = input("Membership ID: ")
    curr.execute("SELECT * FROM Membership WHERE membership_id=?", (id,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("Membership ID does not exist")
        view_member(row)
    else:
        print("=====================================")
        print("Membership ID: " + str(rows[0][0]))
        print("Name: " + str(rows[0][1]))
        print("Email: " + str(rows[0][2]))
        print("Date of Birth: " + str(rows[0][3]))
        print("Gender: " + str(rows[0][4]))
        print("Skill Level: " + str(rows[0][5]))
        print("Plan: " + str(rows[0][6]))
        print("Date: " + str(rows[0][7]))
        print("End Date: " + str(rows[0][8]))
        print("Payment Status: " + str(rows[0][9]))
        print("Membership Status: " + str(rows[0][10]))
        print("======================================")
        menu(row)

def login():
    print("Rock Climbing Membership System")
    username = input("Username: ")
    # checks if username exists in database
    curr.execute("SELECT * FROM Staff WHERE username=?", (username,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("Username does not exist")
        login()
    password = input("Password: ")
    # checks if password matches username
    curr.execute("SELECT * FROM Staff WHERE username=? AND password=?", (username, password))
    rows = curr.fetchall()
    if len(rows) > 0 and rows[0][2] == password:
        row = str(rows[0])
        print("Login Successful")
        print("Welcome " + rows[0][1])
        menu(row)
    else:
        print("Incorrect password")
        login()

login()

import sqlite3
import time 
import datetime

# Connect to database

conn = sqlite3.connect('diary.db')

# Create a cursor

c = conn.cursor()

# Menu

def menu():
    print("Welcome to your diary")
    print("1. Add new entry")
    print("2. View previous entries")
    print("3. Delete entry")
    print("4. Find entry")
    print()

    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        delete_entry()
    elif choice == "4":
        find_entry()
    else:
        print("Invalid choice, try again")
        print()
        menu()



def add_entry():
    print("Add new entry")
    print()

    title = input("Enter title: ")
    content = input("Enter content: ")
    date = datetime.datetime.now()
    c.execute("INSERT INTO diary (title, content, date) VALUES (?, ?, ?)", (title, content, date))


    conn.commit()

    print("Entry added!")
    print()
    menu()


def view_entries():
    print("View previous entries")
    print()

    c.execute("SELECT * FROM diary")
    rows = c.fetchall()

    for row in rows:
        print("Title: ", row[0])
        print("Content: ", row[1])
        print("Date: ", row[2])
        print()

    print()
    menu()


def delete_entry():
    print("Delete entry")
    print()

    title = input("Enter title: ")
    c.execute("SELECT * FROM diary WHERE title=?", (title,))
    row = c.fetchone()
    if row == None:
        print("No entry found to delete")
        print()
        menu()
    

    c.execute("DELETE FROM diary WHERE title=?", (title,))

    conn.commit()

    print("Entry deleted!")
    print()

def find_entry():
    print("Find entry")
    print()

    title = input("Enter title: ")
    c.execute("SELECT * FROM diary WHERE title=?", (title,))
    row = c.fetchone()
    if row == None:
        print("No entry found")
        print()
        menu()
    else:
        print("Title: ", row[0])
        print("Content: ", row[1])
        print("Date: ", row[2])
        print()

    print()
menu()
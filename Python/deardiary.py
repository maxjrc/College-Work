import sqlite3
import datetime
conn = sqlite3.connect("diary.db")

curr = conn.cursor()

def menu():
    while True:
        print("=====================================")
        print("Welcome to the Dear Diary System!")
        op = input("Please select an option: 1. Add Entry 2. Delete Entry 3. Review Entries 4. Exit ")
        if op == "1":
            addentry()
        elif op == "2":
            deleteentry()
        elif op == "3":
            reviewentries()
        elif op == "4":
            print("Goodbye!")
            break
        else:
            print("Not a valid option.")


def addentry():
    title = input("Please enter your title: ")
    content = input("Please enter your content: ")
    date = datetime.datetime.now()
    conn.execute("INSERT INTO diary (title, content, date) VALUES (?, ?, ?)", (title, content, date))
    conn.commit()
    print("Added the entry.")

def deleteentry():
    entry = input("Please enter the title entry you would like to delete: ")
    conn.execute("SELECT * FROM diary WHERE title = ?", (entry,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No Entry found.")
        return
    conn.execute("DELETE FROM diary WHERE title = ?", (entry,))
    conn.commit()
    print("Deleted the entry.")

def reviewentries():
    conn.execute("SELECT * FROM diary")
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No entries found.")
        return
    for row in rows:
        print("=====================================")
        print("Entry: ", row[1])
        print("Date: ", row[2])
        print("=====================================")
    conn.commit()


def find_entry():
    entry = input("Please enter the title entry you would like to find: ")
    conn.execute("SELECT * FROM diary WHERE title = ?", (entry,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No Entry found.")
        return
    for row in rows:
        print("=====================================")
        print("Entry: ", row[1])
        print("Date: ", row[2])
        print("=====================================")
    conn.commit()
menu()


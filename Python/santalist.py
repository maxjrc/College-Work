import sqlite3
import time


conn = sqlite3.connect("santaslist.db")
curr = conn.cursor()


conn.execute("CREATE TABLE IF NOT EXISTS santaslist (name TEXT, naughty TEXT, nice TEXT, year TEXT)")
conn.commit()

def menu():
    print("Welcome to Santa's List!")
    print("1. Add a child to the list")
    print("2. View the list")
    print("3. Search the list")
    print("4. Delete a child from the list")
    print("5. Update a child's status")
    print("6. Delete all children from the list")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == 1:
        name = input("Enter the child's name: ")
        naughty = input("Is the child naughty? ")
        nice = input("Is the child nice? ")
        year = time.strftime("%Y")
        add(name, naughty, nice, year)
        print("Child added to the list!")
        choice = menu()
    elif choice == 2:
        print(view())
        choice = menu()
    elif choice == 3:
        name = input("Enter the child's name: ")
        naughty = input("Is the child naughty? ")
        nice = input("Is the child nice? ")
        year = input("Enter the year: ")
        print(search(name, naughty, nice, year))
        choice = menu()
    elif choice == 4:
        name = input("Enter the child's name: ")
        delete(name)
        print("Child deleted from the list!")
        choice = menu()
    elif choice == 5:
        name = input("Enter the child's name: ")
        naughty = input("Is the child naughty? ")
        nice = input("Is the child nice? ")
        year = input("Enter the year: ")
        update(name, naughty, nice, year)
        print("Child's status updated!")
        choice = menu()
    elif choice == 6:
        deleteall()
        print("All children deleted from the list!")
        choice = menu()
    elif choice == 7:
        exit()

def add(name, naughty, nice, year):
    curr.execute("INSERT INTO santaslist VALUES (?, ?, ?, ?)", (name, naughty, nice, year))
    conn.commit()

def view():
    curr.execute("SELECT * FROM santaslist")
    rows = curr.fetchall()
    return rows

def search(name="", naughty="", nice="", year=""):
    curr.execute("SELECT * FROM santaslist WHERE name=? OR naughty=? OR nice=? OR year=?", (name, naughty, nice, year))
    rows = curr.fetchall()
    return rows

def delete(name):
    curr.execute("DELETE FROM santaslist WHERE name=?", (name,))
    conn.commit()

def update(name, naughty, nice, year):
    curr.execute("UPDATE santaslist SET naughty=?, nice=?, year=? WHERE name=?", (naughty, nice, year, name))
    conn.commit()

def deleteall():
    curr.execute("DELETE FROM santaslist")
    conn.commit()

menu()
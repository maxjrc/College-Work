import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("cafe.db")
curr = conn.cursor()

def createitem():
    name = input("Name: ")
    price = input("Price: ")
    Amount = input("Amount in Stock: ")
    curr.execute("INSERT INTO items (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, Amount))
    conn.commit()
    curr.close()

total_cost = 0
def home_page(user):
  global total_cost
  root = tk.Tk()
  username = user[0]
  root.title(f"CafePOS, {username}")
  root.geometry("600x400")
  welcome_label = tk.Label(root, text=f"Signed on, {username}", font=("Arial", 20))
  welcome_label.pack()
  total_label = tk.Label(root, text=f"Total Cost {total_cost}", font=("Arial", 20))
  total_label.pack()
  items_label = tk.Label(root, text="Items:" )
  items_label.pack(side="left")
  curr.execute("SELECT COUNT(*) FROM items")
  result = curr.fetchone()
  row_count = result[0]
  curr.execute("SELECT * FROM items")
  rows = curr.fetchall()
  for x in range(row_count):
    item_button = tk.Button(root, text=rows[x][0], command=lambda x=x: add_to_total_cost(rows[x][1]))
    item_button.pack(side="left")
  root.mainloop()
def add_to_total_cost(item_cost):
  global total_cost
  total_cost += item_cost
  print("Total Cost:", total_cost)

def login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    curr.execute("SELECT * FROM staff WHERE Username = ? AND Password = ?", (username, password))
    rows = curr.fetchall()
    if len(rows) == 0:  # Check if rows list is empty
       messagebox.showerror("Login Failed", "Invalid username or password")
    else:  
        if username == rows[0][0] and password == rows[0][1]:
            messagebox.showinfo(f"CafePOS {username}", f"Welcome, {username}")
            user = rows[0]
            home_page(user)
    

def main():
    root = tk.Tk()
    root.title("Cafe POS")
    root.geometry("600x400")
    root.resizable(True, True)

    # Create and place the username label and entry
    username_label = tk.Label(root, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    # Create and place the password label and entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")  # Show asterisks for password
    password_entry.pack()

    # Create and place the login button
    login_button = tk.Button(root, text="Login", command=lambda: login(username_entry, password_entry))
    login_button.pack()

    root.mainloop()

main()


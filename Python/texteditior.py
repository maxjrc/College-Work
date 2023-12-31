#import modules
 
from tkinter import *
import sqlite3
import os
import customtkinter
# create a user database
conn = sqlite3.connect("users.db")
curr = conn.cursor()
curr.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL);")
# Designing window for registration

root = customtkinter.CTk()

# Enables Dark Mode
customtkinter.set_appearance_mode("dark")

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    role = "admin"

    conn.execute("INSERT INTO user (username, password, role) VALUES (?, ?, ?)", (username_info, password_info, role))
    conn.commit()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    curr.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username1, password1))
    rows = curr.fetchall()
    if len(rows) > 0:
        password = rows[0][1]
        if password == password1:
            user = rows
            loggedin(user)
        else:
            password_not_recognised()
    else:
        user_not_found()

 
# Designing popup for login success

 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    loggedin_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
def loggedin(user):
    global loggedin_screen
    loggedin_screen = Toplevel(main_screen)
    loggedin_screen.title(f"Hello, {user[0][0]}")
    loggedin_screen.geometry("300x250")
    Label(loggedin_screen, text=f"Hello, {user[0][0]}").pack()
    Button(loggedin_screen, text="OK", command=end_screens).pack()
    if user[0][2] == "admin":
        Label(loggedin_screen, text="You are an admin!").pack()
        Button(loggedin_screen, text="OK", command=adminscreen(user)).pack()


def adminscreen(user):
    if user[0][2] == "admin":
        global aloggedin_screen
        aloggedin_screen = Toplevel(main_screen)
        aloggedin_screen.title(f"Hello, {user[0][0]}")
        aloggedin_screen.geometry("300x250")
        Label(aloggedin_screen, text=f"Hello, {user[0][0]}").pack()
        Button(aloggedin_screen, text="OK", command=end_screens).pack()



def end_screens():
    exit()


main_account_screen()

# update max to say he is an admin

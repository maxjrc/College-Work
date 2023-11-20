import sqlite3
import time 
import random
import os

conn = sqlite3.connect("carsdata.db")

curr = conn.cursor()

curr.execute("CREATE TABLE IF NOT EXISTS Cars (Car_Plate TEXT, Car_Type TEXT, Car_Owner_Name TEXT, Adress TEXT, Average_Speed TEXT)")

conn.commit()

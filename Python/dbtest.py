import sqlite3


conn = sqlite3.connect("memberdata.db")
curr = conn.cursor()

curr.execute("""INSERT INTO Staff (staff_id, username, password, first_name, last_name)
VALUES (1, 'admin', 'admin123', 'John', 'Doe');""")
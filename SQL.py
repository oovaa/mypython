import sqlite3

con = sqlite3.connect("SQL.db")

c = con.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        first_name text,
        last_name text,
        email text
    )      
          """)

# values = [
#     ("tata", "abdo", "tata34@gmail.com"),
#     ("lina", "ahmed", "nana885@gmail.com"),
#     ("3dosh", "mohammed", "3dsha114@gmail.com")DESC
# ]

c.execute(
    "SELECT * FROM customers WHERE email LIKE '%gmail%' ORDER BY first_name DESC LIMIT 2")


[print(x) for x in c.fetchall()]

con.commit()
con.close()
    
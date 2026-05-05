import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# replace with your table name
table = "transactions"

cursor.execute(f"SELECT * FROM {table}")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
c = conn.cursor()

# Get table names
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()

# Print table names and data
for table in tables:
    print(f"Table: {table[0]}")
    c.execute(f"SELECT * FROM {table[0]}")
    data = c.fetchall()
    for row in data:
        print(row)

# Close connection
conn.close()
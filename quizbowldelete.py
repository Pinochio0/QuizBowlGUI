import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
c = conn.cursor()

# Define a list of table names
table_names = ['math1530_questions', 'acct2110_questions','econ2010_questions','db3850_questions','dbmgt3860_questions']  # Add more table names if needed

# Iterate through each table and delete all data
for table_name in table_names:
    c.execute(f"DELETE FROM {table_name}")

# Commit changes and close connection
conn.commit()
conn.close()

print("All data deleted from the database tables.")
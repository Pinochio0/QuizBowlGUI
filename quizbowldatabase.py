import sqlite3

#  Create a connection to the database
conn = sqlite3.connect('quiz_database.db')
c = conn.cursor()

# Create tables for different categories of questions
c.execute('''CREATE TABLE IF NOT EXISTS math1530_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS acct2110_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS econ2010_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS db3850_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS dbmgt3860_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT
             )''')

# Commit changes and close connection
conn.commit()
conn.close()
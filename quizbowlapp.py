import sqlite3
import random

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


# Connect to the database
conn = sqlite3.connect('quiz_database.db')
c = conn.cursor()

# Prompt the user to select a category
print("Select a category:")
print("1. Math 1530")
print("2. Accounting 2110")
print("3. MicroEconomics 2010")
print("4. Business Aplication Development 3850")
print("5. Database  Management 3860")
category_choice = input("Enter the number of the category: ")

# Get questions based on the user's choice
if category_choice == '1':
    category_table = 'math1530_questions'
elif category_choice == '2':
    category_table = 'acct2110_questions'
elif category_choice == '3':
    category_table = 'econ2010_questions'
elif category_choice == '4':
    category_table = 'db3850_questions'
elif category_choice == '4':
    category_table = 'dbmgt3860_questions'
else:
    print("Invalid choice. Exiting...")
    exit()

# Get all questions from the selected category table
c.execute(f"SELECT * FROM {category_table}")
questions = c.fetchall()

# Shuffle the questions
random.shuffle(questions)

# Loop through each question and ask it
for question_data in questions:
    question = question_data[1]
    answer = question_data[2]
    
    # Ask the question and get user input
    print("Question:", question)
    user_answer = input("Your answer: ")

    # Check if the answer is correct
    if user_answer.lower() == answer.lower():
        print(GREEN + "Correct!" + RESET)
    else:
        print(RED + "Incorrect. The correct answer is:", answer + RESET)

# Close connection
conn.close()

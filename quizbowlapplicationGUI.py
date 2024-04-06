from tkinter import *
from tkinter import ttk
import sqlite3
import random

# Constants for colors
GREEN = 'green'
RED = 'red'

class QuizBowlApp():
    def __init__(self, master):
        self.root = master
        self.root.title("Quiz Bowl Application")
        self.root.geometry("500x250+10+10")

        # Connect to the database
        self.conn = sqlite3.connect('quiz_database.db')
        self.c = self.conn.cursor()

        # Welcome message
        self.welcome_label = ttk.Label(root, text="Welcome to Quiz Bowl!", font=("Helvetica", 18))
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Category selection
        self.category_label = ttk.Label(root, text="Select a Category:")
        self.category_label.grid(row=1, column=0, padx=5, pady=5)

        self.category_var = StringVar()
        self.category_options = ["1. Math 1530", "2. Accounting 2110", "3. MicroEconomics 2010", "4. Business Application Development 3850", "5. Database Management 3860"]
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, values=self.category_options,width=40)
        self.category_dropdown.grid(row=1, column=1)

        # Button to start the quiz
        self.start_button = ttk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

    def start_quiz(self):
        # Function to start the quiz
        category_choice = self.category_var.get()[0]  # Extract the number from the category choice

        # Get the table name based on the user's choice
        if category_choice == '1':
            category_table = 'math1530_questions'
        elif category_choice == '2':
            category_table = 'acct2110_questions'
        elif category_choice == '3':
            category_table = 'econ2010_questions'
        elif category_choice == '4':
            category_table = 'db3850_questions'
        elif category_choice == '5':
            category_table = 'dbmgt3860_questions'
        else:
            print("Invalid choice. Exiting...")
            exit()

        # Get all questions from the selected category table
        self.c.execute(f"SELECT * FROM {category_table}")
        self.questions = self.c.fetchall()

        # Shuffle the questions
        random.shuffle(self.questions)

        # Hide the start window
        self.root.withdraw()

        # Open a new window for the quiz
        quiz_window = Toplevel(self.root)
        quiz_window.title("Quiz Window")

        # Initialize variables to keep track of score and current question
        self.current_question_index = 0
        self.correct_answers = 0
        self.total_questions = len(self.questions)

        # Display the first question
        self.display_question(self.questions[self.current_question_index], quiz_window)

    def display_question(self, question_data, window):
    # Destroy any widgets present in the quiz window
        for widget in window.winfo_children():
            widget.destroy()

    # Display feedback from the previous question if available
        if hasattr(self, 'feedback_label'):
            self.feedback_label.destroy()

        if hasattr(self, 'last_feedback'):
            last_feedback_label = ttk.Label(window, text=self.last_feedback[0], font=("Helvetica", 12), foreground=self.last_feedback[1])
            last_feedback_label.grid(row=3, column=0, columnspan=2, pady=5)

        question_label = ttk.Label(window, text="Question: " + question_data[1], font=("Helvetica", 12))
        question_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry for user input
        self.user_answer_entry = ttk.Entry(window)
        self.user_answer_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # Button to submit answer
        submit_button = ttk.Button(window, text="Submit Answer", command=lambda: self.check_answer(question_data[2], window))
        submit_button.grid(row=2, column=0, columnspan=2, pady=5)
        
    def check_answer(self, correct_answer, window):
        # Check if the answer is correct
        user_answer = self.user_answer_entry.get().strip().lower()
        if user_answer == correct_answer.lower():
            self.last_feedback = ("Correct!", GREEN)
            self.correct_answers += 1
        else:
            self.last_feedback = ("Incorrect. The correct answer is: " + correct_answer, RED)

        # Move to the next question or end the quiz
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.display_question(self.questions[self.current_question_index], window)
        else:
            self.display_final_score(window)

    def display_feedback(self, message, color, window):
        feedback_label = ttk.Label(window, text=message, font=("Helvetica", 12), foreground=color)
        feedback_label.grid(row=3, column=0, columnspan=2, pady=5)

    def display_final_score(self, window):
        final_score_label = ttk.Label(window, text="Quiz Finished!\nYour Score: {}/{}".format(self.correct_answers, self.total_questions), font=("Helvetica", 16))
        final_score_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Destroy the quiz window
        self.root.deiconify()

        # Close connection
        self.conn.close()

root = Tk()
app = QuizBowlApp(root)
root.mainloop()
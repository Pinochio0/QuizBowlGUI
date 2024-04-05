import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
c = conn.cursor()

# Insert data into the math1530_questions table
math1530_data = [
    ("In a class of 30 students, what is the mean (average) number of siblings per student?", 1.5),
    ("A company conducted a survey of its employees' ages. If the median age is 35 years, what is the age of the employee at the 75th percentile?", 42),
    ("The heights of a group of 50 students are measured. If the standard deviation of heights is 4 inches, what is the variance of heights in square inches?", 16),
    ("A factory produces 500 items per day on average with a standard deviation of 20 items. What is the coefficient of variation for the daily production?", 4),
    ("The time taken by a commuter to reach the office follows a normal distribution with a mean of 45 minutes and a standard deviation of 5 minutes. What is the z-score for a commute time of 40 minutes?", -1),
    ("The scores of a test are normally distributed with a mean of 75 and a standard deviation of 10. What is the 90th percentile score?", 88),
    ("A group of 25 students took a math test. The mean score was 80 with a standard deviation of 8. What is the sum of the scores?", 2000),
    ("The weights of bags of rice in a shipment are normally distributed with a mean of 50 kg and a standard deviation of 2 kg. What is the probability that a randomly selected bag weighs more than 54 kg?", 0.1587),
    ("The monthly salaries of employees in a company are normally distributed with a mean of $4000 and a standard deviation of $500. What is the 75th percentile salary?", 4472.41),
    ("A group of 40 students took a science quiz. If the mode of quiz scores is 85, how many students scored 85?", 2)
]

c.executemany('''INSERT INTO math1530_questions (question, answer)
                 VALUES (?, ?)''', math1530_data)

acct2110_data = [
    ("What is the process of recording financial transactions?", "Bookkeeping"),
    ("What is the total amount of money owed to a company?", "Accounts Receivable"),
    ("What is the total amount of money owed by a company?", "Accounts Payable"),
    ("What is the term for the net income after taxes?", "Profit"),
    ("What is the monetary value of a company's liabilities subtracted from its assets?", "Equity"),
    ("What is the financial statement that shows a company's revenues and expenses over a period?", "Income Statement"),
    ("What is the document that summarizes a company's financial position at a specific point in time?", "Balance Sheet"),
    ("What is the financial statement that shows a company's cash inflows and outflows?", "Cash Flow Statement"),
    ("What is the process of examining a company's financial statements?", "Auditing"),
    ("What is the term for an organization's obligation to pay a debt in the future?", "Liability")
]

c.executemany('''INSERT INTO acct2110_questions (question, answer)
                 VALUES (?, ?)''', acct2110_data)

econ2010_data = [
    ("What is the study of choices people make to attain their goals, given their scarce resources?", "Economics"),
    ("What term refers to the total value of goods and services produced in a country in a given period?", "GDP"),
    ("Which economic system relies on private ownership of the means of production?", "Capitalism"),
    ("What is the opposite of a surplus?", "Shortage"),
    ("What do we call the measure of responsiveness of quantity demanded to a change in price?", "Elasticity"),
    ("What is the term for the total amount of money held by the public, including currency and demand deposits?", "M1"),
    ("What is the opposite of inflation?", "Deflation"),
    ("What economic principle states that as consumption increases, marginal utility decreases?", "Diminishing"),
    ("What term describes the level of output at which total revenue equals total cost?", "Break-even"),
    ("What is the study of how resources are allocated to satisfy human wants?", "Microeconomics")
]

c.executemany('''INSERT INTO econ2010_questions (question, answer)
                 VALUES (?, ?)''', econ2010_data)

db3850_data = [
    ("What programming language is commonly used for business applications development?", "Java"),
    ("Which software development methodology emphasizes incremental and iterative development?", "Agile"),
    ("What technology facilitates communication between different software applications?", "APIs"),
    ("What type of database management system is frequently utilized in business applications?", "Relational"),
    ("What approach ensures that software remains functional across various devices and screen sizes?", "Responsive Design"),
    ("What process ensures that software updates are seamlessly delivered to users?", "Continuous Deployment"),
    ("What practice involves automating repetitive tasks in the software testing process?", "Test Automation"),
    ("What security measure encrypts data transmitted over the internet?", "SSL/TLS"),
    ("What cloud computing service model allows users to rent virtualized hardware resources?", "Infrastructure as a Service (IaaS)"),
    ("What type of software license permits users to view and modify the source code?", "Open Source")
]

c.executemany('''INSERT INTO db3850_questions (question, answer)
                 VALUES (?, ?)''', db3850_data)

dbmgt3860_data = [
    ("What is a collection of related data organized in a way that facilitates efficient retrieval?", "Database"),
    ("What is the unique identifier for a record in a database table?", "Primary Key"),
    ("What is the process of ensuring that data remains accurate and consistent over time?", "Validation"),
    ("What type of database model organizes data into tables with rows and columns?", "Relational"),
    ("What is a database operation used to retrieve specific data from a table?", "Query"),
    ("What is a software application used to interact with a database?", "Interface"),
    ("What is the language used to manipulate and query databases?", "SQL"),
    ("What is a set of rules that defines the structure and organization of a database?", "Schema"),
    ("What is a database design technique that reduces data redundancy?", "Normalization"),
    ("What is a database constraint that ensures data integrity by restricting the values that can be inserted into a column?", "Check Constraint")
]

c.executemany('''INSERT INTO dbmgt3860_questions (question, answer)
                 VALUES (?, ?)''', dbmgt3860_data)

# Commit changes and close connection
conn.commit()
conn.close()
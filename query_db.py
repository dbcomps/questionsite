import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Query the questions table
c.execute('SELECT * FROM questions')
questions = c.fetchall()
print("Questions:", questions)

# Query the answers table
c.execute('SELECT * FROM answers')
answers = c.fetchall()
print("Answers:", answers)

# Close the connection
conn.close()
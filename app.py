from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime
import sqlite3
from collections import Counter

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS questions (date TEXT PRIMARY KEY, question TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS answers (date TEXT, answer TEXT)')
    conn.commit()
    conn.close()

init_db()

# Function to get today's question
def get_todays_question():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    c.execute('SELECT question FROM questions WHERE date = ?', (today,))
    question = c.fetchone()
    conn.close()
    if question:
        return question[0]
    return "No question for today!"

# Function to summarize answers
def summarize_answers():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    c.execute('SELECT answer FROM answers WHERE date = ?', (today,))
    answers = c.fetchall()
    conn.close()
    answers = [answer[0] for answer in answers]
    summary = Counter(answers).most_common()
    return summary

# Routes
@app.route('/')
def index():
    question = get_todays_question()
    summary = summarize_answers()
    return render_template('index.html', question=question, summary=summary)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form['answer']
    today = datetime.today().strftime('%Y-%m-%d')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO answers (date, answer) VALUES (?, ?)', (today, answer))
    conn.commit()
    conn.close()
    return jsonify({"message": "Answer submitted!"})

@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        date = request.form['date']
        question = request.form['question']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO questions (date, question) VALUES (?, ?)', (date, question))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_question.html')

@app.route('/clear_answers', methods=['POST'])
def clear_answers():
    today = datetime.today().strftime('%Y-%m-%d')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM answers WHERE date = ?', (today,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Answers cleared!"})

if __name__ == '__main__':
    app.run(debug=True)

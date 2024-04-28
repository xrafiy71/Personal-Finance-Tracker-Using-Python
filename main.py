from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        amount REAL,
                        description TEXT
                    )''')
    conn.commit()
    conn.close()

# Route to add a new expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    description = request.form['description']

    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO expenses (category, amount, description)
                      VALUES (?, ?, ?)''', (category, amount, description))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Route to display all expenses
@app.route('/')
def index():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses''')
    expenses = cursor.fetchall()
    conn.close()

    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

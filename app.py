# app.py
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS sums (id INTEGER PRIMARY KEY AUTOINCREMENT, value INTEGER)')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get the number entered by the user
            number = int(request.form['number'])
            
            # Update the database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO sums (value) VALUES (?)', (number,))
            conn.commit()
            conn.close()
        except ValueError:
            # Handle invalid input if the user entered something other than a number
            pass

    # Retrieve the running sum from the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(value) FROM sums')
    running_sum = cursor.fetchone()[0]
    conn.close()

    # If no data in the database, set the running_sum to 0
    if running_sum is None:
        running_sum = 0

    return render_template('index.html', running_sum=running_sum)

@app.route('/reset', methods=['POST'])
def reset():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Delete all records from the 'sums' table
    cursor.execute('DELETE FROM sums')
    conn.commit()
    conn.close()

    # Redirect back to the index page after resetting the count
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

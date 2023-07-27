# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to store the running sum
running_sum = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global running_sum
    
    if request.method == 'POST':
        try:
            # Get the number entered by the user
            number = int(request.form['number'])
            # Update the running sum
            running_sum += number
        except ValueError:
            # Handle invalid input if the user entered something other than a number
            pass
        
    return render_template('index.html', running_sum=running_sum)

if __name__ == '__main__':
    app.run(debug=True)


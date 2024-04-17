# Import necessary libraries
from flask import Flask, render_template

# Creating Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)

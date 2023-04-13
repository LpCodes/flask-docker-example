# Import the Flask class from the flask module
from flask import Flask, render_template

# Create a new instance of Flask and store it in the variable 'app'
app = Flask(__name__)

# Define a route for the default URL, which returns an HTML page
@app.route('/')
def hello_world():
    return render_template('index.html')

# Run the app if this file is executed
if __name__ == '__main__':
    # Set the debug mode to true and listen on all IP addresses
    app.run(debug=True, host='0.0.0.0')

# app.py

from flask import Flask
from waitress import serve

app = Flask(__name__)

# Route to the root URL
@app.route('/')
def hello():
    return 'Hello, Flask on Docker!'

# Route to a custom endpoint
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to Flask on Docker.'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=6000)
    serve(app, host="0.0.0.0", port=3000)

# Flask template 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Flask template</h1>'

if __name__ == '__main__':
    app.run(debug=True)
from sys import get_coroutine_origin_tracking_depth
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hello, {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{num * word}"

if __name__ == "__main__":
    app.run(debug=True)

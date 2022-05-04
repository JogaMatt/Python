from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard():
    return render_template("index.html")

@app.route('/<x>/<y>')
def customBoard(x, y):
    row = int(x)
    col = int (y)
    return render_template("index.html", row=row, col=col)

if __name__ == "__main__":
    app.run(debug=True)
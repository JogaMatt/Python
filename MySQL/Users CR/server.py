from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)

@app.route('/')
@app.route('/allusers')
def users():
    return render_template("read(all).html", users = User.get_all())

@app.route('/allusers/new')
def addUsers():
    return render_template("create.html")

@app.route('/allusers/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/allusers')

if __name__ == "__main__":
    app.run(debug=True)
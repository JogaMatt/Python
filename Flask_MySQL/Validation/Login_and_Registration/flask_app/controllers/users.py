import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['name'] = request.form['first_name']
    return redirect("/homepage")

@app.route('/login', methods=['POST'])
def login():
    data = { 
        "email" : request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name
    return redirect("/homepage")

@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    return render_template('homepage.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
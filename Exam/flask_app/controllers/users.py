from dataclasses import dataclass
import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.magazine import Magazine
from flask_app.controllers import magazines


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
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
    return redirect("/dashboard")

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
    return redirect("/dashboard")

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    data = {
        'id': id
    }
    magazines = Magazine.get_all_magazines()

    return render_template('/edit.html', users = User.get_one(data), magazines = magazines)

@app.route('/update_user',methods=['POST'])
def update():
    print(request.form)
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    if not User.validate_update(request.form):
        return redirect(f"/edit/{request.form['id']}")

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": session['user_id']
    }
    User.update(data)

    session.clear()
    
    data = { 
        "email" : request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

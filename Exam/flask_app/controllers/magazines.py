import re
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.magazine import Magazine
from flask_app.models.user import User


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    magazines = Magazine.get_all_magazines()
    users = User.get_all_users()
    return render_template('dashboard.html', magazines = magazines, users = users)

@app.route('/magazine/<int:id>')
def magazine(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    data = {
        'id':id
    }

    return render_template('/magazines.html', magazines = Magazine.get_one(data))

@app.route('/create')
def create():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    return render_template('/create.html')

@app.route('/post_magazine', methods=['POST'])
def post_magazine():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    if not Magazine.validate_magazine(request.form):
        return redirect('/create')

    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "user_id": session['user_id'],
    }

    Magazine.save(data)

    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_magazine(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    data = {
        "id": id
    }
    Magazine.delete(data)
    return redirect('/dashboard')



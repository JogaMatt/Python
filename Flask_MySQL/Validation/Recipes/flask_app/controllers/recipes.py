import re
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', recipes = recipes)

@app.route('/instructions/<int:id>')
def instructions(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    data = {
        'id':id
    }

    return render_template('/recipes.html', recipes = Recipe.get_one(data))

@app.route('/create')
def create():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    return render_template('/create.html')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    data = {
        'id':id
    }

    return render_template('/edit.html', recipes = Recipe.get_one(data))

@app.route('/post_recipe', methods=['POST'])
def post_recipe():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect('/create')

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "cook_time" : request.form['cook_time'],
        "made_on" : request.form['made_on'],
        "user_id": session['user_id']
    }

    Recipe.save(data)

    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')
    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/update_recipe/<int:id>',methods=['POST'])
def update(id):
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/{id}")

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "cook_time" : request.form['cook_time'],
        "user_id": session['user_id'],
        'id': id
    }
    Recipe.update(data)


    return redirect('/dashboard')

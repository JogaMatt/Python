from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Survey

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route("/result")
def result():
    return render_template("result.html", survey = Survey.get_last_survey())
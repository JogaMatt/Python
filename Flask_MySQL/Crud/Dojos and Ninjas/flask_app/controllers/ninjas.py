from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')

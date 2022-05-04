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
    return redirect('/')

@app.route('/')
@app.route('/users/<int:id>')
def show_info(id):
    data = {
        "id":id
    }
    return render_template("show_info.html", user=User.get_one(data))

@app.route('/users/edit/<int:id>')
def edit_info(id):
    data = {
        "id":id
    }
    return render_template("edit_info.html", user=User.get_one(data))

@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
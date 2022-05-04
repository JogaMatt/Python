from flask import Flask, render_template
app = Flask(__name__)

# import statements, maybe some other routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return "Success!"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<string:name>/<int:num>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(name, num):
    return render_template("hello.html",name=name, num=num)



    
# app.run(debug=True) should be the very last statement! 



if __name__ == "__main__":
    app.run(debug=True)
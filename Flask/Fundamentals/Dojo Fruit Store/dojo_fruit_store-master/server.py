from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/',  methods=['GET'])         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return request.form

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)
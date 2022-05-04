from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template('success.html', emails = emails)

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    Email.save(request.form)
    return redirect('/success')

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/success')



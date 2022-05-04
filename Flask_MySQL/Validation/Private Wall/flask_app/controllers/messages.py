from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.message import Message

@app.route('/send', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        flash("Please sign in/register")
        return redirect('/')

    if not Message.validate_message(request.form):
        return redirect('/wall')

    data = {
        "message": request.form['message'],
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id']
    }

    Message.save(data)

    return redirect('/wall')
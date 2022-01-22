from flask import Blueprint, request, session, redirect, render_template
from models.user import get_user_by_email
import bcrypt

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

@session_controller.route('/login')
def loginpage():
    error = request.args.get('error', None)
    return render_template('login.html', error=error)

@session_controller.route('/sessions/create', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = get_user_by_email(email)
    valid = user and bcrypt.checkpw(password.encode(), user['password'].encode())
    if valid:
        session['user_id'] = user['id']
        session['user_name'] = user['name']
        return redirect('/')
    else:
        return redirect('/login?error=Incorrect+username+or+password')

@session_controller.route('/sessions/destroy', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect('/')
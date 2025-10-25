from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/Logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up')
def sign_up():
    return "<p>sign up</p>"


#debug
@auth.route('/auth')
def auth():
    new_user = User(email="test@email.com",password="",first_name="Bill",last_name="Will",access_key="10706~V6ArtwADBUtD9tCYCfJkQP8neRWMyVZW2AXED7CNRWZzx9JP2PEANVBha9zDmyNW")
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('views.home'))
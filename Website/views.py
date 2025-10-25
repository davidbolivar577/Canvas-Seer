from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/home')
def home2():
    return redirect(url_for('/'))

"""
@views.route('/home')
def home2():
    return render_template("home_2.html")

"""
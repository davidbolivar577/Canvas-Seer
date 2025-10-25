from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('views.home'))

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/login')
def login(login_status):
    #if logged in
    if (login_status):
        return redirect(url_for('views.home'))
    return render_template("login_page.html")

@views.route('/signup')
def signup():
    #if logged in
    return render_template("sign_up.html")

@views.route('/logout')
def logout(login_status):
    if (login_status):
        return redirect(url_for('views.home'))
    return render_template("logout.html")

@views.route('/settings')
def settings():
    return render_template("settings.html")

@views.route('/calendar/')
def calendar():
    return redirect(url_for('views.calM'))

@views.route('/calendar/monthly')
def calM():
    return render_template("calendar_month.html")

@views.route('/calendar/weekly')
def calW():
    return render_template("calendar_week.html")

@views.route('/calendar/list')
def calL():
    return render_template("calendar_list.html")

@views.route('/courses')
def courses():
    return render_template("courses.html")

@views.route('/courses/<course>')
def course(course):
    return render_template("course.html", course)

@views.route('/courses/<course>/<module>')
def module(course, module):
    return render_template("module.html", path = [course, module])

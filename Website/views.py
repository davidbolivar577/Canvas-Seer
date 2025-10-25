from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('views.home'))

#todo #6
@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/login')
def login(login_status):
    #if logged in
    if (login_status):
        return redirect(url_for('home.html'))
    return render_template("login_page.html")

@views.route('/signup')
def signup():
    #if logged in
    return render_template("sign_up.html")

@views.route('/logout')
def logout(login_status):
    if (login_status):
        return redirect(url_for('home.html'))
    return render_template("logout.html")

@views.route('/settings')
def settings():
    return render_template("settings.html")

@views.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@views.route('/calendar/monthly')
def calM():
    return render_template("calendarMonthly.html")

@views.route('/calendar/weekly')
def calW():
    return render_template("calendarWeekly.html")

@views.route('/calendar/list')
def calL():
    return render_template("calendarList.html")

@views.route('/courses')
def courses():
    return render_template("courses.html")

@views.route('/courses/?')
def courseNum(course_number):
    return render_template(url_for('courses/?',values=course_number))

@views.route('/courses/?/??')
def module():
    return render_template("courses/?/??.html")

"""
@views.route('/home')
def home2():
    return render_template("home_2.html")

"""
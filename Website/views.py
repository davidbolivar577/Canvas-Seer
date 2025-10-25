from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import json
views = Blueprint('views', __name__)

login_status = False

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
            login_status = True

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
'''
@views.route('/')
def root():
    return redirect(url_for('views.home'))

@views.route('/home')
def home():
    return render_template("home.html")
'''

@views.route('/login')
def login():
    #if logged in
    if (login_status):
        return redirect(url_for('views.home'))
    return render_template("login_page.html")

@views.route('/signup')
def signup():
    #if logged in
    return render_template("sign_up.html")

@views.route('/logout')
def logout():
    if (login_status == False):
        return redirect(url_for('login_page.home'))
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



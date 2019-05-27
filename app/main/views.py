from flask import render_template, abort, request,redirect,url_for
from . import main
from flask_login import login_required
# Views
@main.route('/')
def index():

    name="!Pitch"
    title="Welcome| Pitch your idea in one minutes!"
    return render_template('index.html', name=name)
@main.route('/about')
def about_app():
    message="This is an app where you get to pitch your idea for one minute then other users can rate yout pitch. You also get to rate other people's idea. How cool is that!!!"

    return render_template('about.html',message=message)

@main.route('/piches')
def see_pitches():

    name="!Pitch"
    title="Welcome| Pitch your idea in one minutes!"
   

    return render_template('pitches.html',title=title, name=name)

@main.route('/pitches/comments/')
@login_required
def post_comment():

    return render_template ('comment.html', title=title, name=name)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
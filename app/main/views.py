from flask import render_template
from . import main

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
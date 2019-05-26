from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    name="!Pitch"
    title="Welcome| Pitch your idea in one minutes!"
    return render_template('index.html', name=name)

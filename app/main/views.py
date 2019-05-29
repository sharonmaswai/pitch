from flask import render_template, abort, request,redirect,url_for
from . import main
from flask_login import login_required, current_user
from .. import db,photos
from .forms import PitchForm, CommentForm

from ..models import User, Pitch, Comments

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

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_pitch():
   

    name="!Pitch"
    title="Welcome| Pitch your idea in one minute!"

    form=PitchForm()
    
    if form.validate_on_submit():

        title=form.title.data
        content=form.pitch.data
        category =form.category.data
        upvote=0
        downvote=0
        new_pitch = Pitch(title=title, category=category, content=content, upvote=upvote, downvote=upvote )

        new_pitch.save_pitch()
        return redirect(url_for('main.post_pitch'))
    
   

    
    return render_template('pitches.html',title = title, name=name, form=form)

    

@main.route('/posts/')


def post_pitch():

    pitches=Pitch.query.all()


    return render_template ('posts.html', pitches=pitches)
@main.route('/comments/<id>',methods = ['GET', 'POST'])
def post_comment(id):
    pitch = Pitch.query.filter_by(id=id).first()
    
    form = CommentForm()
    
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        
        new_comment = Comments(comment_title = title, comment = comment, pitch_id=id, posted_by=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('.post_comment',id=pitch.id))
    return render_template('comments.html',form=form, pitch=pitch)
    


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

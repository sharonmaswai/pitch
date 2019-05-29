from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Business','Business'),('Event','Event'),('Technology','Technology')],validators=[Required()])
    submit = SubmitField('PITCH')

class CommentForm(FlaskForm):
    
    
    title = StringField('Comment')
    comment = TextAreaField('Enter your comment')
    submit = SubmitField('submit')

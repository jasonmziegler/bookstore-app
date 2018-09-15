from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):
    name = StringField("What's your name?")
    email = StringField('Enter your email address.')
    submit = SubmitField('Register')

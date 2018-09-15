from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                               ValidationError)

class RegistrationForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired(), Length(3,15,message="Between 3 and 15 characters")])
    email = StringField('Enter your email address.', validators=[DataRequired(),Email()])
    password = PasswordField('Enter a password', validators=[DataRequired(),Length(5),EqualTo('Confirm',message="passwords must match")])
    confirm = PasswordField('Confirm your password', validators=[DataRequired()])
    submit = SubmitField('Register')

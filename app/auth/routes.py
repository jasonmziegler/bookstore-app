#app/auth/routes.py

from  flask import render_template, request
from app.auth.forms import RegistrationForm
from app.auth import authentication as at

@at.route('/register')
def register_user():
    form = RegistrationForm()
    return render_template('registration.html', form=form)

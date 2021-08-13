from flask import render_template, request
from app.auth.forms import RegistrationForm
from app.auth import authentication as at  #this is the blueprint

@at.route('/register', methods=['GET','POST'])
def register_user():
    name = None
    email = None
    form = RegistrationForm()

    #this is ran after pressing submit button
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data

    return render_template('registration.html', form=form, name=name, email=email)
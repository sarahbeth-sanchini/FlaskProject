from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):

    name = StringField("Please enter your name: ")
    email = StringField("Please enter your email: ")
    submit = SubmitField("Click Here to Register")
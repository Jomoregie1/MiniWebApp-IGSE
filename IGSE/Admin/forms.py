from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from IGSE import models
from IGSE.models import Customer


# TODO 1: add functionality to retrieve password if lost.
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords do '
                                                                                                     'not match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    Property_type = RadioField('Property type', choices=[('1', 'Detached'), ('2', 'Semi-detached'), ('3', 'Terraced'),
                                                         ('4', 'Flat'), ('5', 'Cottage'), ('6', 'Bungalow'),
                                                         ('7', 'Mansion')])
    Number_of_rooms = IntegerField('Number of rooms', validators=[DataRequired()])
    Evc = IntegerField('Evc code', validators=[DataRequired()])
    Submit = SubmitField('Register')

    # This is used to check if a user already exist by checking if the email entered in the form already exisit.
    def check_email(self, email):
        if Customer.query.filer_by(Customerid=email.data).first():
            raise ValidationError('Your email has already been registered')

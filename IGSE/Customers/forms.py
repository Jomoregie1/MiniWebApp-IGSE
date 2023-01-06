from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, RadioField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email
from email_validator import validate_email
from wtforms import ValidationError
from IGSE.error_pages import handlers

from flask_login import current_user
from IGSE.models import Customer


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must '
                                                                                                     'match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    property_type = RadioField('Property type', choices=[('detached', 'Detached'), ('semi-detached', 'Semi-detached'),
                                                         ('terraced', 'Terraced'),
                                                         ('flat', 'Flat'), ('cottage', 'Cottage'),
                                                         ('bungalow', 'Bungalow'),
                                                         ('mansion', 'Mansion')])
    bedroom_num = IntegerField('Number of rooms', validators=[DataRequired()])
    evc = IntegerField('Evc code', validators=[DataRequired()])
    submit = SubmitField('Register')

    # TODO this may cause a bug and is used to throw an error if the user has entered an email that exist already.
    def check_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            return handlers.error_409()

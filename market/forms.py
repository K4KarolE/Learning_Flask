from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import Email
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):     # Flaskform -> validate_ -> field name(username) --> search for username   // function naming important
        user = User.query.filter_by(username=username_to_check.data).first()     # checking if there is a user with the sam username already
        if user:
            raise ValidationError('Username already exists! Please try a different one.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address alredy exists! Please use a different one.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])    # for password confirmation field
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password1 = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
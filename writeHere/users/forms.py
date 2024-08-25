from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from flask_login import current_user


#ownclass
from writeHere.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        userFind = User.query.filter_by(username=username.data).first()

        if userFind:
            raise ValidationError("That username is taken. Please choose another one")

    def validate_email(self,email):
        emailFind = User.query.filter_by(email=email.data).first()

        if emailFind:
            raise ValidationError("That email is taken. Please choose another one")


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')





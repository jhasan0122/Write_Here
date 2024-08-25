from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import current_user,login_user

#ownclass--
from writeHere.models import User, Post
from writeHere.users.forms import RegistrationForm, LoginForm
from writeHere import bcrypt, db

users = Blueprint('users',__name__)

@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    regForm = RegistrationForm()
    if regForm.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(regForm.password.data).decode('utf-8')
        userObj = User(username=regForm.username.data, email=regForm.email.data, password=hashed_password)
        db.session(userObj)
        db.session.commit()
        flash('Your account has been created!, You are now able to login','success')
        return redirect(url_for('main.home'))
    return render_template('register.html',title='Register',form=regForm)


@users.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    regForm = LoginForm()
    if regForm.validate_on_submit():
        userFind = User.query.filter_by(email=regForm.email.data).first()
        if userFind and bcrypt.check_password_hash(userFind.password, regForm.password.data):
            login_user(userFind,remember=regForm.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash("Login unsuccessful. Please check your email and password ",'danger')

    return render_template('login.html',form=regForm,title='Login')

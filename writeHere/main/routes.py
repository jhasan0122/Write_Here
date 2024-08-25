
from flask import Blueprint, render_template


main = Blueprint('main',__name__,template_folder='C:\\Users\\HP TECHNOLOGY\\Write_Here\\writeHere\\templates')

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html',title='Home')

@main.route('/about')
def about():
    return render_template('about.html',title='About')
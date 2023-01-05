from flask import Blueprint, render_template, request
from IGSE import db

customer = Blueprint('customer', __name__)


@customer.route('/login')
def login():
    return render_template('login.html')


@customer.route('/signup')
def signup():
    return render_template('register.html')


@customer.route('/logout')
def logout():
    return render_template('logout.html')

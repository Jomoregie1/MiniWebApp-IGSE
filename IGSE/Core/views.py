from flask import render_template, request, Blueprint, url_for, flash, redirect
from flask_login import login_user, logout_user
from IGSE import db
from IGSE.models import Customer, Admin
from IGSE.Core.forms import LoginForm

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.data.email
        admin = Admin.query.filter_by(email=email).first()
        if admin is None:
            user = Customer.query.filter_by(email=email).first()
            if user.check_user(password=form.data.password) and user is not None:
                login_user(user)
                flash('Successfully logged in!')
                return redirect(url_for('core.index'))
        else:
            if admin.check_admin(password=form.data.password):
                login_user(admin)
                flash('Successfully logged in!')
                return render_template('admin/index.html')

    return render_template('login.html', form=form)


@core.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.login"))

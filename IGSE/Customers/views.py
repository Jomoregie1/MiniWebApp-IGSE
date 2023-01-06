from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from IGSE import db
from IGSE.models import Customer, Reading, Voucher
from IGSE.Customers.forms import RegistrationForm, LoginForm

customer = Blueprint('customer', __name__)


@customer.route('/login')
def login():
    return render_template('login.html')


@customer.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Customer(name=form.name.data,
                        email=form.email.data,
                        password=form.password.data,
                        address=form.address.data,
                        property_type=form.property_type.data,
                        bedroom_num=form.bedroom_num.data,
                        evc=form.evc.data)

        db.session.add(user)
        db.session.commit()
        flash(f'Thanks {form.name.data}, for registering.')
        return redirect(url_for('users.login'))

    return render_template('register.html')


@customer.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

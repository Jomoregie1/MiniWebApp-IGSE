from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from IGSE import db
from IGSE.models import Customer, Reading, Voucher
from IGSE.Customers.forms import RegistrationForm, LoginForm

customer = Blueprint('customer', __name__)


@customer.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.data.email).first()

        if user.check_user(password=form.data.password) and user is not None:
            login_user(user)
            flash('Successfully logged in!')

            # This checks if the user was trying to access a page that required a login. if that is true the value of next is set to that page.
            next = request.args.get('next')

            # This condition check if the user was in fact trying to access another page, if they weren't then it returns them to the homepage.
            if next is None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)


@customer.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    form.submit = 'Sign up'

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

    return render_template('register.html', form=form)


@customer.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

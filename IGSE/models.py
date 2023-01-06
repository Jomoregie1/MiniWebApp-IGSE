from IGSE import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(email):
    return Customer.query.get(email)


class Customer(db.Model, UserMixin):

    __tablename__ = 'Customer'

    customer_id = db.Column(db.String(64), primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    address = db.Column(db.Text, nullable=False)
    property_type = db.Column(db.String, nullable=False)
    bedroom_num = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    type = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    readings = db.relationship('Reading', backref='customer', lazy=True)
    vouchers = db.relationship('Voucher', backref='customer', lazy=True, uselist=False)

    def __init__(self, name, email, address, password, property_type, bedroom_num, evc):
        self.name = name
        self.customer_id = email
        self.password_hash = generate_password_hash(password)
        self.address = address
        self.property_type = property_type
        self.bedroom_num = bedroom_num
        Voucher.EVC_code = evc

    def check_user(self, password):
        return check_password_hash(self.Password_hash, password)

    def __str__(self):
        return f'Email of user: {self.customer_id}'


class Admin(db.Model):
    """Model for GSE admin account."""
    __tablename__ = 'admin'

    email = db.Column(db.String(255), primary_key=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __str__(self):
        return f'Admin {self.email}.'

    def check_admin(self, password):
        """Check if provided password matches admin's password."""
        return check_password_hash(self.Password_hash, password)


def create_admin_account(email, password):
    """Create initial admin account with provided email and password."""
    admin = Admin(email=email, password=password)
    db.session.add(admin)
    db.session.commit()


class Reading(db.Model):
    __tablename__ = 'Reading'

    """ Used to create readings model in the database """
    reading_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(64), db.ForeignKey('Customer.customer_id'))
    submission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    elec_readings_day = db.Column(db.Float, nullable=False)
    elec_readings_night = db.Column(db.Float, nullable=False)
    gas_reading = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    bill_amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False, nullable=False)

    # TODO 1a create this function calculate_bill_amount to set the value of the bill_amount
    # TODO 1b Might have to create a utils.py to hold this function in the customer directory.
    # def set_bill_amount(self):
    #     """Set bill amount for reading."""
    #     self.bill_amount = calculate_bill_amount(self)


class Tariff(db.Model):
    __tablename__ = 'Tariff'

    """ Used to create tariff model in the database """
    tariff_type = db.Column(db.String, primary_key=True)
    rate = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)


class Voucher(db.Model):
    __tablename__ = 'Voucher'

    """ Used to create voucher model in the database """
    EVC_code = db.Column(db.String(64), primary_key=True)
    customer_id = db.Column(db.String(64), db.ForeignKey('Customer.customer_id'))
    used = db.Column(db.Boolean, nullable=False)

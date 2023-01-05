# from IGSE import db, login_manager
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
#
#
# @login_manager.user_loader
# def load_user(email):
#     if email == 'gse@shangrila.gov.un':
#         return Admin.query.get('gse@shangrila.gov.un')
#     return Customer.query.get(email)
#
#
# class Customer(db.Model, UserMixin):
#     __tablename__ = 'Customers'
#
#     Customerid = db.Column(db.String(64), primary_Key=True)
#     Password_hash = db.Column(db.String(128))
#     Address = db.Column(db.Text)
#     PropertyType = db.Column(db.String)
#     NumberOfBedrooms = db.Column(db.Integer)
#     EVC = db.Column(db.Integer)
#
#     def __init__(self, email, address, password, propertyType, numberOfBedrooms, evc):
#         self.Customerid = email
#         self.Address = address
#         self.Password_hash = generate_password_hash(password)
#         self.PropertyType = propertyType
#         self.NumberOfBedrooms = numberOfBedrooms
#         self.EVC = evc
#
#     def check_user(self, password):
#         return check_password_hash(self.Password_hash, password)
#
#
# class Admin(db.Model, UserMixin):
#     __tablename__ = 'Admin'
#
#     Adminid = db.Column(db.String(64), primary_key=True)
#     Password_hash = db.Column(db.String(128))
#
#     def __init__(self,email,password):
#         self.Adminid = email
#         self.Password_hash = password
#
#     def check_user(self, password):
#         return check_password_hash('gse@energy', password)
#





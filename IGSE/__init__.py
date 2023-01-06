import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from IGSE.error_pages.handlers import error_pages
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


login_manager = LoginManager()

# app config --------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"

# Database setup -------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'customers.login'

# Admin setup ------------------------------
from IGSE.models import Reading
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')
admin.add_view(ModelView(Reading, db.session))

# adding blueprints -----------------------------------
from IGSE.Core.views import core

app.register_blueprint(core)
app.register_blueprint(error_pages)
from IGSE.Customers.views import customer

app.register_blueprint(customer)

from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/signup')
def register():
    return render_template('register.html')

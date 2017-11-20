from flask import render_template
from flask_login import login_required
from . import bp_about
# from .. import db
from ..models import User, Role


@bp_about.route('/')
def index():
    a = User.query.filter_by(username='tom').first()

    return render_template('about/dbshow.html', role=a.role.name, username=a.username)


@bp_about.route('/1')
@login_required
def index1():
    return render_template('about/index.html')


@bp_about.route('/2')
def index2():
    return render_template('about/index.html')


@bp_about.route('/3')
def index3():
    return render_template('about/index.html')



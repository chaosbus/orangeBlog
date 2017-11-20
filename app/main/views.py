from flask import render_template
from . import bp_main


@bp_main.route('/')
def index():
    return render_template('main/index.html')



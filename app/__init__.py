# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_nav import Nav
# from flask_nav.elements import Navbar, View, Subgroup, Separator
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # bootstrap
    bootstrap.init_app(app)
    # db
    db.init_app(app)
    # login
    login_manager.init_app(app)
    # blueprint
    from .main import bp_main
    app.register_blueprint(bp_main, url_prefix='/')
    from .about import bp_about
    app.register_blueprint(bp_about, url_prefix='/about')
    from .auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    return app

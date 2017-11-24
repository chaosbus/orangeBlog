# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_nav import Nav
# from flask_nav.elements import Navbar, View, Subgroup, Separator
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_misaka import Misaka
from flask_flatpages import FlatPages
from config import config
# from pygments_ext import PygmentsExtension
from .xbox import jinja_filter_custom

mail = Mail()
misaka = Misaka()
bootstrap = Bootstrap()
db = SQLAlchemy()
pages = FlatPages()
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
    # email
    mail.init_app(app)
    # misaka
    misaka.init_app(app)
    # flatpages
    pages.init_app(app)
    jinja_filter_custom.init_app(app)

    # blueprint
    from .main import bp_main
    app.register_blueprint(bp_main, url_prefix='/')
    from .about import bp_about
    app.register_blueprint(bp_about, url_prefix='/about')
    from .auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    # app.jinja_env.add_extension(PygmentsExtension)

    return app

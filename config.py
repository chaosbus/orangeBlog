# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'NjQwNzdlOWZmYmE0ZTNmOTQ1MWNhOGM4YjA4NzhiMGMgIC0K'
    SSL_DISABLE = False
    # sqlalchemy {
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    # }
    # mail {
    MAIL_SERVER = 'smtp.mxhichina.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True,
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'blog@solodisplay.com'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = 'Dswybsmm999'
    MAIL_DEFAULT_SENDER = 'no-reply <blog@solodisplay.com>'
    ORANGE_MAIL_SUBJECT_PREFIX = u'[橙色的皮蛋]'
    # }
    # flatpages {
    FLATPAGES_ROOT = 'docs'
    FLATPAGES_EXTENSION = '.md'
    # FLATPAGES_ENCODING = 'utf8'
    # FLATPAGES_HTML_RENDERER = ''
    FLATPAGES_MARKDOWN_EXTENSIONS = ['toc', 'codehilite', 'headerid']
    FLATPAGES_AUTO_RELOAD = True
    # }
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False



class ConsumeConfig(Config):
    # DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-cnsm.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'consume': ConsumeConfig,
    'default': DevelopmentConfig
}


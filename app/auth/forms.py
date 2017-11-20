# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    account = StringField(u'帐号/邮箱/手机1', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')


class RegisterForm(FlaskForm):
    username = StringField(u'', validators=[DataRequired()])
    email = StringField(u'', validators=[DataRequired(), Email()])




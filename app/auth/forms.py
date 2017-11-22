# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    account = StringField(u'帐号/邮箱/手机..', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码..', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我..')
    submit = SubmitField(u'登陆..')


class RegisterForm(FlaskForm):
    username = StringField(u'帐号', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'只允许字母，数字，下划线，点号')])
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(4, 64), EqualTo('password2', message=u'密码不一致')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'该用户名已注册')

# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from flask import request
from flask_login import login_user, logout_user, login_required
from flask_login import current_user
from . import bp_auth
from .forms import LoginForm, RegisterForm
from ..models import User
from .. import db
from ..email import send_email


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'登陆失败')
    return render_template('auth/login.html', form=form)


@bp_auth.route('/login1', methods=['GET', 'POST'])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Login failed')
    return render_template('auth/login1.html', form=form)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'登出成功')
    return redirect(url_for('main.index'))


@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        token = user.generate_confirmation_token()
        send_email(user.email, u'邮件确认', 'auth/email/confirm', user=user, token=token)
        flash(u'注册成功')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


# @bp_auth.route('/register1', methods=['GET', 'POST'])
# def register1():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data, username=form.username.data, password=form.password.data)
#         db.session.add(user)
#         flash(u'注册成功')
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register1.html', form=form)


@bp_auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash(u'邮件确认成功。')
    else:
        flash(u'邮件确认失败，请确认是否合法或已失效')
    return redirect(url_for('main.index'))


# @bp_auth.before_app_request
# def before_request():
#     """
#     FIXME，没有确认不能浏览是否合理？
#     """
#     if current_user.is_authenticated \
#             and not current_user.confirmed \
#             and request.blueprint != 'auth' \
#             and request.endpoint != 'static':
#         return redirect(url_for('auth.unconfirmed'))


@bp_auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@bp_auth.route('/confirm')
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, u'邮件确认重发', 'auth/email/confirm', user=current_user, token=token)
    flash(u'新确认邮件已发送。')
    return redirect(url_for('main.index'))


# @bp_auth.route('/qlogin')
# def login_simple():
#     return render_template('auth/login_simple.html')
#
#
# @bp_auth.route('/qregister')
# def register_simple():
#     return render_template('auth/register_simple.html')


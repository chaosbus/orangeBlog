from flask import render_template, redirect, url_for, flash
from flask import request
from flask_login import login_user, logout_user, login_required
from . import bp_auth
from .forms import LoginForm, RegisterForm
from ..models import User


@bp_auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Login failed')
    return render_template('auth/login.html', form=form)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success')
    return redirect(url_for('main.index'))


@bp_auth.route('/qlogin')
def login_simple():
    return render_template('auth/login_simple.html')


@bp_auth.route('/register')
def register():
    return render_template('auth/register.html')


@bp_auth.route('/qregister')
def register_simple():
    return render_template('auth/register_simple.html')


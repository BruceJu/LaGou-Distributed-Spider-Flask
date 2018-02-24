# coding:utf8
from functools import wraps

from flask import render_template, redirect, url_for, flash, session, request

from forms import LoginForm
from . import admin
from ..model import Admin


def admin_logon_request(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login' or request.url))
        return function(*args, **kwargs)

    return decorated_function


@admin.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        data = loginForm.data
        record = Admin.query.filter_by(account=data['account']).first()
        if not record.check_pwd(data['pwd']):
            flash('密码错误')
            return redirect(url_for('admin.login'))
        else:
            # 构造session
            session['admin'] = data['account']
            print(session)
            return redirect(url_for('admin.index' or request.args["next"]))

    return render_template('admin/login.html', form=loginForm)


@admin.route('/logout')

def logout():
    session['admin'].pop()
    return redirect(url_for('admin.login'))


@admin.route('/')
@admin_logon_request
def index():
    return 'hello'

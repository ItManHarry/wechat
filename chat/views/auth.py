from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from chat.forms import LoginForm
from chat.models import User, Log
from chat.tools import redirect_back
from chat.plugins import db
import uuid
#系统授权
bp_auth = Blueprint('auth', __name__)
@bp_auth.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        code = form.code.data
        password = form.password.data
        user = User.query.filter_by(code=code.lower()).first()
        if user:
            if user.validate_password(password):
                login_user(user, True)
                #写入登录履历
                log = Log(id=uuid.uuid4().hex, user_id=user.id, action='登录')
                db.session.add(log)
                db.session.commit()
                return redirect_back()
            else:
                flash('密码错误！')
        else:
            flash('账号不存在!')
    return render_template('auth/login.html', form=form)
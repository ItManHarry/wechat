from flask import Blueprint, render_template
#系统授权
bp_auth = Blueprint('auth', __name__)
@bp_auth.route('/login')
def login():
    return render_template('auth/login.html')
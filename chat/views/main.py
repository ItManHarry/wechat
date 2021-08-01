from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
bp_main = Blueprint('main', __name__)
@bp_main.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('main/index.html')
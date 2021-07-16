from flask import Blueprint
#系统授权
bp_auth = Blueprint('auth', __name__)
@bp_auth.route('/')
def index():
    return '<h1>Auth View.</h1>'
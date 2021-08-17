from flask import Blueprint, abort, url_for, redirect, flash
from flask_login import current_user
from chat.plugins import oauth, db
from werkzeug import security
import os
bp_oauth = Blueprint('oauth', __name__)
#http://127.0.0.1/oauth/github/callback/
#client id:5d2aa3fceb9730bda5c5
#client secret:d0dc99c5dc841c8043e065d5996d2e9e1787fea3
github = oauth.remote_app(
    name='github',
    consumer_key=os.getenv('GITHUB_CLIENT_ID'),
    consumer_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    request_token_params={'scope': 'user', 'state': lambda: security.gen_salt(10)},
    base_url='https://api.github.com',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)
providers = {
    'github': github
}
#跳转至第三方认证网址
@bp_oauth.route('/login/<provider_name>')
def login(provider_name):
    if provider_name not in providers:
        abort(404)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    callback = url_for('.callback', provider_name=provider_name, _external=True)
    return providers[provider_name].authorize(callback=callback)
@bp_oauth.route('/<provider_name>/callback')
def callback(provider_name):
    if provider_name not in providers:
        abort(404)
    provider = providers[provider_name]
    response = provider.authorized_response()
    if response is not None:
        access_token = response.get('access_token')
    else:
        access_token = None
    print('Access token is : %s' %access_token)
    if access_token is None:
        flash('认证失败,请重试！')
        return redirect(url_for('main.home'))
    return redirect(url_for('main.home'))
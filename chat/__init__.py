from flask import Flask, render_template
from chat.config import setting
from chat.plugins import db, moment
# 动态创建App实例
def create_app(setting_name=None):
    if setting_name == None:
        setting_name = 'dev_setting'
    app = Flask('chat')
    app.config.from_object(setting[setting_name])
    register_app_global_url(app)
    register_app_plugins(app)
    register_app_views(app)
    return app
def register_app_global_url(app):
    @app.route('/chat/index')
    def index():
        return '<h1>Chat Index</h1>'
    @app.route('/ui/index')
    def ui():
        return render_template('ui/index.html')
def register_app_plugins(app):
    db.init_app(app)
    moment.init_app(app)
def register_app_views(app):
    from chat.views.auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')
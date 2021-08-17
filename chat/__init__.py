from flask import Flask, render_template, redirect, url_for
import click, uuid
from chat.config import settings
from chat.plugins import db, moment, socketio, login_manager, oauth
from chat.models import User
# 动态创建App实例
def create_app(setting=None):
    if setting == None:
        setting = 'dev_setting'
    app = Flask('chat')
    app.config.from_object(settings[setting])
    register_app_global_url(app)
    registe_app_global_context(app)
    register_app_plugins(app)
    register_app_shell_context(app)
    register_app_views(app)
    register_app_commands(app)
    return app
def register_app_global_url(app):
    @app.route('/')
    def index():
        return redirect(url_for('main.home'))
    @app.route('/ui/index')
    def ui():
        user = User.query.first()
        return render_template('ui/index.html', user=user)
def registe_app_global_context(app):
    from chat.tools import get_time, format_time
    @app.context_processor
    def app_global_context():
        return dict(get_time=get_time, format_time=format_time)
def register_app_plugins(app):
    db.init_app(app)
    moment.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)
    oauth.init_app(app)
def register_app_shell_context(app):
    @app.shell_context_processor
    def app_shell_context():
        return dict(db=db)
def register_app_views(app):
    from chat.views.auth import bp_auth
    from chat.views.main import bp_main
    from chat.views.oauth import bp_oauth
    app.register_blueprint(bp_auth, url_prefix='/auth')
    app.register_blueprint(bp_main, url_prefix='/main')
    app.register_blueprint(bp_oauth, url_prefix='/oauth')
def register_app_commands(app):
    @app.cli.command()
    @click.option('--username', prompt=True, help='管理员账号')
    @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='管理员密码')
    def init(username, password):
        click.echo('执行数据库初始化')
        db.create_all()
        click.echo('数据库初始化完成')
        click.echo('创建系统管理员')
        user = User.query.first()
        if user:
            click.echo('管理员已存在,跳过创建')
        else:
            user = User(
                id=uuid.uuid4().hex,
                code=username.lower(),
                name=username.lower(),
                email='jack_chengqian@163.com'
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            click.echo('管理员已创建')
        click.echo('系统初始化完成')
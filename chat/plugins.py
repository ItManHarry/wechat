from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user
from flask_oauthlib.client import OAuth
db = SQLAlchemy()
moment = Moment()
socketio = SocketIO()
oauth = OAuth()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = '登录后才能进行相关操作!!!'
login_manager.login_message_category = 'warning'
@login_manager.user_loader
def load_user(user_id):
    from chat.models import User
    user = User.query.get(user_id)
    return user
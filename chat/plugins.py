from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user
db = SQLAlchemy()
moment = Moment()
socketio = SocketIO()
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    from chat.models import User
    user = User.query.get(user_id)
    return user
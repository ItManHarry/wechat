import uuid
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask_socketio import emit
from flask_login import login_required
from chat.plugins import socketio, db
from chat.models import Message
from datetime import datetime
#主聊天室
bp_main = Blueprint('main', __name__)
online_users = []   #当前在线人数
anonymous_users = 0 #匿名在线人数
@bp_main.route('/home')
def home():
    return render_template('main/home.html')
@bp_main.route('/index')
@login_required
def index():
    return render_template('main/index.html')
@bp_main.route('/anonymous')
def anonymous():
    return render_template('main/anonymous.html')
#主聊天室 - 登录
@socketio.on('new message')
def new_message(message_str):
    print('New message send ...')
    message = Message(
        id=uuid.uuid4().hex,
        content=message_str,
        sender_id=current_user.id
    )
    db.session.add(message)
    db.session.commit()
    emit('new message', {'message_html': render_template('main/_message.html', message=message)}, broadcast=True)
#匿名聊天室 - 无需登录
@socketio.on('new message', namespace='/anonymous')
def anonymous_new_message(message):
    emit('new message', {'message_html': render_template('main/_anonymous_message.html', message=message, time=datetime.utcnow())}, broadcast=True, namespace='/anonymous')
@socketio.on('connect')
def connect():
    global online_users
    if current_user.is_authenticated and current_user.id not in online_users:
        online_users.append(current_user.id)
    emit('user count', {'count': len(online_users)}, broadcast=True)

@socketio.on('connect', namespace='/anonymous')
def anonymous_connect():
    global anonymous_users
    anonymous_users += 1
    emit('anonymous user count', {'count': anonymous_users}, broadcast=True, namespace='/anonymous')
@socketio.on('disconnect')
def disconnect():
    global online_users
    if current_user.is_authenticated and current_user.id in online_users:
        online_users.remove(current_user.id)
    emit('user count', {'count': len(online_users)}, broadcast=True)
@socketio.on('disconnect', namespace='/anonymous')
def anonymous_disconnect():
    global anonymous_users
    anonymous_users -= 1
    emit('anonymous user count', {'count': anonymous_users}, broadcast=True, namespace='/anonymous')
import uuid
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from flask_socketio import emit
from chat.plugins import socketio, db
from chat.models import Message

bp_main = Blueprint('main', __name__)
@bp_main.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('main/index.html')
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
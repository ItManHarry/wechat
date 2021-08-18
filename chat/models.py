from chat.plugins import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
import hashlib
'''
    系统用户
'''
class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    code = db.Column(db.String(32), unique=True, index=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    email_hash = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    website = db.Column(db.String(32))
    github = db.Column(db.String(32))
    bio = db.Column(db.Text())
    messages = db.relationship('Message', back_populates='sender', cascade='all')
    logs = db.relationship('Log', back_populates='user', cascade='all')
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_email_hash()
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
    def generate_email_hash(self):
        if self.email is not None and self.email_hash is None:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
    #头像
    @property
    def gravatar(self):
        return 'https://gravatar.com/avatar/%s?d=monsterid' %self.email_hash
'''
    消息
'''
class Message(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    content = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    sender = db.relationship('User', back_populates='messages')
'''
    登录履历
'''
class Log(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)
    action = db.Column(db.String(128))
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='logs')
from chat.plugins import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    timestamp = db.Column(db.DateTime, defautl=datetime.utcnow(), index=True)
    code = db.Column(db.String(32), unique=True, index=True)
    name = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
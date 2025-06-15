from app import db
from datetime import datetime

class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username        = db.Column(db.String(50), nullable=False, unique=True)
    email           = db.Column(db.String(50), nullable=False)
    password        = db.Column(db.String(50))
    created_at      = db.Column(db.DateTime)
    updated_at      = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User {self.username}>'
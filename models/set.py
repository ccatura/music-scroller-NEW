from app import db

class Set(db.Model):
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title           = db.Column(db.String(50), nullable=False, unique=True)
    subtitle        = db.Column(db.String(50), nullable=False, unique=True)
    artist          = db.Column(db.String(50), nullable=False)
    album           = db.Column(db.String(50), nullable=False)
    genre           = db.Column(db.String(50), nullable=False)
    year            = db.Column(db.Integer, nullable=False)
    lyrics          = db.Column(db.Text, nullable=False)
    created_at      = db.Column(db.DateTime)
    updated_at      = db.Column(db.DateTime)

    # owner           = db.relationship('User', backref='set', lazy=True)

    def __repr__(self):
        return f'<Song title={self.title}, id={self.id}>'
    
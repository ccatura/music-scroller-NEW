from app import db

class Song(db.Model):
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title           = db.Column(db.String(50), nullable=False)
    subtitle        = db.Column(db.String(50), nullable=True)
    artist          = db.Column(db.String(50), nullable=False)
    album           = db.Column(db.String(50), nullable=True)
    genre           = db.Column(db.String(50), nullable=True)
    year            = db.Column(db.Integer, nullable=True)
    lyrics          = db.Column(db.Text, nullable=False)
    created_at      = db.Column(db.DateTime)
    updated_at      = db.Column(db.DateTime)

    owner           = db.relationship('User', backref='songs', lazy=True)
    owner_id        = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Song title={self.title}, id={self.id}>'
    
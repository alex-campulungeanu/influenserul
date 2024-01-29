from datetime import datetime
from app import db


class QuoteModel(db.Model):
    __tablename__ = 'quote'
    id = db.Column(db.Integer(), primary_key=True)
    body = db.Column(db.String(500), unique=True)
    active = db.Column(db.Integer(), default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Quote %r>" % (self.id)
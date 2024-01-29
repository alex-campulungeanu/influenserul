from datetime import datetime

from app import db, ma


class PlatformModel(db.Model):
    __tablename__ = 'platform'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    posts = db.relationship('PostPlatformModel', back_populates='platform')

    def  __repr__(self):
        return "<Platform %r>" % (self.name)
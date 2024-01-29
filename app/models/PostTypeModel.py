from datetime import datetime

from app import db, ma


class PostTypeModel(db.Model):
    __tablename__ = 'post_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def  __repr__(self):
        return "<PostType %r>" % (self.name)
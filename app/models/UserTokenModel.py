from app import db

class UserTokenModel(db.Model):
    __tablename__ = 'user_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return "<UserTokenModel %r>" % (self.token)
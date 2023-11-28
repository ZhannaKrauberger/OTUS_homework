from .database import db


class WishList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, default="My wishes")
    description = db.Column(db.Text)
    secret = db.Column(db.Boolean, default=False)

    author = db.Column(db.Integer)  # связь с юзером

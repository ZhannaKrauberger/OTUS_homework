from datetime import datetime

from .database import db


class WishList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, default="My wishes")
    description = db.Column(db.Text)
    secret = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # связь с юзером

    def __repr__(self):
        return f"wishlist: id={self.id} name={self.name} user: id={self.user_id}"

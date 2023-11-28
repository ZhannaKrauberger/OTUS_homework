from datetime import datetime

from .database import db


# TODO: как хранить email?
# TODO: нормально ли хранить цену в float?
class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    wishlist_id = db.Column(
        db.Integer, db.ForeignKey("wish_list.id")
    )  # связь с вишлистом, который связан с юзером

    def __repr__(self):
        return f"wish: id={self.id} name={self.name} wishlist: id={self.wishlist_id}"

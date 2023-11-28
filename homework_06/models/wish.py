from .database import db


# TODO: как хранить email?
# TODO: нормально ли хранить цену в float?
class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    price = db.Column(db.Float)

    wishlist = db.Column(db.Integer)  # связь с вишлистом, который связан с юзером

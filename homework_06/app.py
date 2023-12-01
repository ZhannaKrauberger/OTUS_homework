from os import getenv

from flask import Flask, render_template, request, flash
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

from models import WishList
from models.database import db
from models.user import User

app = Flask(__name__)

config_name = getenv("CONFIG NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")


db.init_app(app=app)
migrate = Migrate(app=app, db=db)


@app.route("/sign_up/", methods={"POST", "GET"}, endpoint="sign_up")
def sign_up():
    if request.method == "POST":
        hash_password = generate_password_hash(request.form["password"])
        user = User(
            first_name=request.form["firstName"],
            last_name=request.form["lastName"],
            username=request.form["username"],
            email=request.form["email"],
            password=hash_password,
        )
        db.session.add(user)
        db.session.flush()

        wishlist = WishList(user_id=user.id)
        db.session.add(wishlist)
        db.session.commit()

    return render_template("sign_up.html")


@app.route("/sign_in/")
def sign_in():
    return render_template("sign_in.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/create/")
def create():
    return render_template("create.html")


@app.route("/find/")
def find():
    return render_template("find.html")


@app.route("/wishlists/")
def wishlists():
    return render_template("my_wishlist.html")


@app.route("/support/", methods={"GET", "POST"})
def support():
    if request.method == "POST":
        # TODO: нужны нормальные проверки
        if len(request.form["email"]) > 2:
            flash("Message sent :)")
        else:
            flash("Error :(")
    return render_template("support.html")


@app.errorhandler(code_or_exception=404)
def page_not_found(error):
    return render_template("page404.html")

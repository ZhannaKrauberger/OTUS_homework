from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from models.database import db

app = Flask(__name__)

config_name = getenv("CONFIG NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")


db.init_app(app=app)
migrate = Migrate(app=app, db=db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/sign_in/")
def sign_in():
    return render_template("sign_in.html")


@app.route("/sign_up/", endpoint="sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/create/")
def create():
    return render_template("create.html")


@app.route("/find/")
def find():
    return render_template("find.html")


@app.route("/wishlists/")
def wishlists():
    return render_template("my_wishlist.html")


@app.route("/support/")
def support():
    return render_template("support.html")

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

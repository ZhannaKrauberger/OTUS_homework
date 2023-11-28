from os import getenv

from flask import Flask, render_template

app = Flask(__name__)

config_name = getenv("CONFIG NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")

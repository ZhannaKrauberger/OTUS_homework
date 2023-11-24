from flask import Flask, render_template, request, url_for, redirect
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.get("/")
def get_index():
    return render_template("index.html")


@app.route("/about_me/", endpoint="about_me")
def get_my_name():
    name = request.form.get("my-name")
    print(name)




@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")

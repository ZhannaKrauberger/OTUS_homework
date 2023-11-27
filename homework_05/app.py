from flask import Flask, render_template, request, url_for, redirect
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.get("/", endpoint="home")
def get_index():
    return render_template("index.html")


@app.route("/about_me/", methods={"GET", "POST"}, endpoint="about_me")
def create_my_name():
    if request.method == 'POST':
        name = request.form['name']
        greeting_message = f"Hi, {name.title()} :)"
        return render_template("about_me.html", message=greeting_message)
    return render_template("about_me.html")


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")

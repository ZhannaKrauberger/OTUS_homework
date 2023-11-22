from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def get_index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")

from flask import render_template
from app import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", name="Home")


@app.route("/contact")

def contact():
    return render_template("contact.html")


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

#second part of main.py in set-up video
from flask import Flask, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
#from .models import Item
# ^^from .models import [Class_Name]

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)
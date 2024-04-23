#second part of main.py in set-up video
from flask import Flask, redirect, url_for, render_template, request

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
#from .models import Item
# ^^from .models import [Class_Name]

users = {}
print(users)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username=request.form['username']
        print(f'requesting username: {username}')
        if username in users:
            print('username already exists')
            return render_template("register.html")
        else:
            users[username] = request.form['password']
            print(f'user {username} created')
            print(users)
            return render_template('homepage.html')
    else:
        return render_template('register.html')

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)
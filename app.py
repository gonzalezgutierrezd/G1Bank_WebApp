#second part of main.py in set-up video
from flask import Flask, redirect, url_for, render_template, request

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db
#from .models import Item
# ^^from .models import [Class_Name]
from functions import Bank

users = {}
print(users)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            print(f'Loging in as { username }')
            return render_template('homepage.html')
        elif username not in users:
            print(f'User {username} not found')
            return render_template("loginfailure.html")
        elif  users[username] != password:
            print('Incorrect password.')
            return render_template("loginfailure.html")
        else:
            print('Login failed.')
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
            return render_template('login.html')
    else:
        return render_template('register.html')

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    ## sample of how this could be used
    
    bankInstance = Bank('Eli')
    print(bankInstance.show_details())

    #deposite to bank instance
    print(bankInstance.deposit(1000))
    print(bankInstance.show_details())

    #withdraw from bank instance
    print(bankInstance.withdraw(100))
    print(bankInstance.show_details())
    
    return render_template("withdraw.html")
    


if __name__ == "__main__":
    app.run(debug=True)


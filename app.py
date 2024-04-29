#second part of main.py in set-up video
from flask import Flask, redirect, url_for, render_template, request

from flask_sqlalchemy import SQLAlchemy
from __init__ import app
#from .models import Item
# ^^from .models import [Class_Name]
import database as db
from functions import Bank

users = db.getUsers()
print(users)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if username.casefold() == user.get_username().casefold() and user.get_password() == password:
                print(f'Logging in as {username}')
                return redirect(url_for('user', username=user.get_username().casefold()))
            elif username.casefold() == user.get_username().casefold() and user.get_password() != password:
                print(f'Password: {password}, User password: {user.get_password()}')
                print('Incorrect password.')
                return render_template("loginfailure.html")
        print('Login failed.')
    return render_template("login.html")

@app.route("/<username>", methods=['GET','POST'])
def user(username):
    if request.method == 'POST':
        print("user\t" + username)
        user = db.get_user_by_username(username)
        accounts = user.get_accounts()
        if user is not None and accounts is not None:
            return redirect(url_for('account', username=username))
    return render_template("user.html", username=username)

@app.route("/<username>/<int:account_id>", methods=['GET','POST'])
def account(username, account_id):
    user = db.get_user_by_username(username)
    accounts = user.get_accounts()
    for account in accounts:
        if account.id == account_id:
            accountV = account
            transactions = account.get_transactions()
            return render_template("account.html", user=user, accounts=accounts, transactions=transactions, account_id=account_id, accountV=accountV)
    return "Account not found"

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        print(f'Requesting username: {username}')
        if username is not None:
            for user in users:
                if user.get_username() is not None and user.get_username().casefold() == username.casefold():
                    print('Username already exists')
                    return redirect(url_for('login'))
            if username and password and firstName and lastName:
                db.create_user(firstName, lastName, username, password, 0)
                print(f'User {username} created')
                return redirect(url_for('login'))
        else:
            print('Missing information')
            return redirect(url_for('register'))
        
    return render_template('register.html')

@app.route("/register2", methods=['POST'])
def register2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        
        if username and password and firstName and lastName:
            db.create_user(firstName, lastName, username, password, 0)
            print(f'User {username} created')
            return redirect(url_for('login'))
        else:
            print('Missing information')
            return redirect(url_for('register'))
    return render_template('register2.html')

@app.route("/deposit")
def deposit():
    """
    ## Sample of how this could be used
    # Make instance
    bankInstance = Bank('userName')
    print(bankInstance.show_details())
    # Deposit to bank instance
    print(bankInstance.deposit(1000))
    print(bankInstance.show_details())
    # Withdraw from bank instance
    print(bankInstance.withdraw(100))
    print(bankInstance.show_details())
    """
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)

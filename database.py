from datetime import datetime
from platform import release
from random import Random, randint
import random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BOOLEAN, create_engine, ForeignKey, Column, String, Integer, CHAR, table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import request
import sqlite3
from sqlalchemy import Float
from sqlalchemy.orm import relationship
Base = declarative_base()
engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
        __tablename__ = 'user'
        id = Column("id", Integer, primary_key=True)
        fName = Column("fName", String)
        lName = Column("lName", String)
        username = Column("uName", String)
        password = Column("password", String)
        balance = Column("balance", Float)
        accounts = relationship("Accounts", backref="user")

        def __init__ (self, id, fName, lName, username, password, balance, accounts):
            self.id = id
            self.fName = fName
            self.lName = lName
            self.username = username
            self.password = password
            self.balance = balance
            self.accounts = accounts

        def __str__(self):
            return f"<User('{self.id}', '{self.fName}', '{self.lName}', '{self.username}', '{self.password}', '{self.balance}', '{self.accounts}')>"

        # Getters and Setters
        def get_id(self):
            return self.id

        def set_id(self, id):
            self.id = id

        def get_fName(self):
            return self.fName

        def set_fName(self, fName):
            self.fName = fName

        def get_lName(self):
            return self.lName

        def set_lName(self, lName):
            self.lName = lName

        def get_username(self):
            return self.username

        def set_username(self, username):
            self.username = username

        def get_password(self):
            return self.password

        def set_password(self, password):
            self.password = password

        def get_balance(self):
            return self.balance

        def set_balance(self, balance):
            self.balance = balance

        def get_accounts(self):
            return self.accounts

        def set_accounts(self, accounts):
            self.accounts = accounts

class Accounts(Base):
    __tablename__ = 'accounts'
    id = Column("id", Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    accountNumber = Column("accountNumber", Float(32), unique=True)
    accountType = Column("accountType", String)
    balance = Column("balance", Float)
    transactions = relationship("Transaction", backref="accounts")
    
    def __init__ (self, id, user_id, accountNumber, accountType, balance, transactions):
        self.id = id
        self.user_id = user_id
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = balance
        self.transactions = transactions

    # Getters and Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_accountNumber(self):
        return self.accountNumber

    def set_accountNumber(self, accountNumber):
        self.accountNumber = accountNumber

    def get_accountType(self):
        return self.accountType

    def set_accountType(self, accountType):
        self.accountType = accountType

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_transactions(self):
        return self.transactions

    def set_transactions(self, transactions):
        self.transactions = transactions

class Transaction(Base):
        __tablename__ = 'transaction'
        id = Column("id", Integer, primary_key=True)
        amount = Column("amount", Float(precision=2))
        date = Column("date", String)
        toAccount = Column("toAccount", String)
        account_id = Column(Integer, ForeignKey('accounts.id'))

        def __init__ (self, id, amount, date, account_id):
            self.id = id
            self.amount = amount
            self.date = date
            self.account_id = account_id

        def __str__(self):
            return f"<Transaction('{self.id}', '{self.amount}', '{self.date}', '{self.account_id}')>"

        # Getters and Setters
        def get_id(self):
            return self.id

        def set_id(self, id):
            self.id = id

        def get_amount(self):
            return self.amount

        def set_amount(self, amount):
            self.amount = amount

        def get_date(self):
            return self.date

        def set_date(self, date):
            self.date = date

        def get_toAccount(self):
            return self.toAccount

        def set_toAccount(self, toAccount):
            self.toAccount = toAccount

        def get_account_id(self):
            return self.account_id

        def set_account_id(self, account_id):
            self.account_id = account_id
class Admin(Base):
        __tablename__ = 'admin'
        id = Column("id", Integer, primary_key=True)
        fName = Column("fName", String)
        lName = Column("lName", String)
        username = Column("uName", String)
        password = Column("password", String)

        def __init__ (self, id, fName, lName, username, password):
            self.id = id
            self.fName = fName
            self.lName = lName
            self.username = username
            self.password = password
            

        def __str__(self):
            return f"<Admin('{self.id}', '{self.fName}', '{self.lName}', '{self.username}', '{self.password}')>"

def create_example_data():

    # Create 100 unique example user objects
    for i in range(1, 101):
        new_user = User(None, fName=f"User{i}", lName="Doe", username=f"user{i}", password="password", balance=1000.0, accounts=[])
        session.add(new_user)

        # Create 3 example accounts for each user
        for j in range(1, 4):
            new_account = Accounts(None, new_user, None, accountType="Savings", balance=500.0, transactions=[])
            session.add(new_account)

            # Create 20 example transactions for each account
            for k in range(1, 21):
                new_transaction = Transaction(None, amount=random.uniform(1.0, 100.0), date=datetime.now().strftime("%Y-%m-%d"), account_id=None)
                session.add(new_transaction)

                new_account.transactions.append(new_transaction)

            new_user.accounts.append(new_account)

def flush_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
def print_user(user):
    print(f"User ID: {user.id}")
    print(f"First Name: {user.fName}")
    print(f"Last Name: {user.lName}")
    print(f"Username: {user.username}")
    print(f"Password: {user.password}")
    print(f"Balance: {user.balance}")
    print("Accounts:")
    for account in user.accounts:
        print(f"\tAccount Number: {account.accountNumber}")
        print(f"\tAccount Type: {account.accountType}")
        print(f"\tBalance: {account.balance}")
        print("Transactions:")
        print("\n")
        for transaction in account.transactions:
            print(f"\t\tTransaction ID: {transaction.id}")
            print(f"\t\tAmount: {transaction.amount}")
            print(f"\t\tDate: {transaction.date}")
            print(f"\t\tTo Account: {transaction.toAccount}")
            print("\n")
    print("\n")
def create_user(fName, lName, username, password, balance):
    new_user = User(None, fName=fName, lName=lName, username=username, password=password, balance=balance, accounts=[])
    session.add(new_user)
    session.commit()
    return new_user
def create_account(user_id, accountNumber, accountType, balance):
    new_account = Accounts(None, user_id, accountNumber, accountType, balance, [])
    session.add(new_account)
    session.commit()
def create_transaction(amount, date, account_id):
    new_transaction = Transaction(None, amount, date, account_id)
    session.add(new_transaction)
    session.commit()
    return new_transaction
def get_user_by_username(username):
    return session.query(User).filter_by(username = username).first()
def getUsers():
    return session.query(User).all()
def getDatabase():
    return session
def main():
    for user in session.query(User).all():
        print_user(user)
      

if __name__ == "__main__":
    main()

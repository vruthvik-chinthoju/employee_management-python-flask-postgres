from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Manager(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(1500),nullable=False)
    employees = db.relationship('Employee',backref='manager',lazy=True)


class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    department = db.Column(db.String(150),nullable=False)
    salary = db.Column(db.Integer,nullable=False)
    manager_id = db.Column(db.Integer,db.ForeignKey('manager.id'),nullable=False)


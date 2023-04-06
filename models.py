import peewee as pw
from database import BaseModel


class User(BaseModel):
    surname = pw.CharField(unique=True)
    group = pw.CharField()


class Machine(BaseModel):
    name = pw.CharField(unique=True)


class Instructions(BaseModel):
    machine = pw.ForeignKeyField(Machine, backref='instructed')
    user = pw.ForeignKeyField(User, backref='instructions')
    date = pw.DateTimeField()

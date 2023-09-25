from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db

class Route(db.Model):
    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True)
    route_code = db.Column(db.Integer)
    route_path = db.Column(db.String)

    def __repr__(self):
        return f'<{self.id}>'
    
class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String)
    quantity = db.Column(db.Integer)
    route = db.Column() # assosiation from routes
    total_price = db.Column(db.Integer)
    total_cost = db.Column(db.Integer)

class Machines(db.Model):
    __tablename__ = "machines"

    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String)

class Workers(db.Model):
    __tablename = "workers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

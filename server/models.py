from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db

class Route(db.Model):
    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True)
    tool_type = db.Column(db.String)
    coating_type = db.Column(db.String)
    step_1 = db.Column(db.String)
    step_2 = db.Column(db.String)
    step_3 = db.Column(db.String)
    step_4 = db.Column(db.String)
    step_5 = db.Column(db.String)
    step_6 = db.Column(db.String)
    step_7 = db.Column(db.String)
    step_8 = db.Column(db.String)
    step_9 = db.Column(db.String)
    step_10 = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<{self.id}>'
    
# class Orders(db.Model):
#     __tablename__ = "orders"

#     id = db.Column(db.Integer, primary_key=True)
#     item_type = db.Column(db.String)
#     quantity = db.Column(db.Integer)
#     route = db.Column() # assosiation from routes
#     total_price = db.Column(db.Integer)
#     total_cost = db.Column(db.Integer)

# class Machines(db.Model):
#     __tablename__ = "machines"

#     id = db.Column(db.Integer, primary_key=True)
#     machine_name = db.Column(db.String)

# class Workers(db.Model):
#     __tablename = "workers"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

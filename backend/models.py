import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, Float, ARRAY, TIMESTAMP
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

# Database for Pickos

# TODO:
'''
 -- Implement User Side (means instantiation of User Table to access certain orders)
'''

# Changelog:
'''
 -- Version 0.1.0 Creator
     -- Init Creation
     -- Currently only restaurant side active
 -- Version 0.2.0 Creator
     -- Star Schema fixes
     -- Currently only restaurant side active
 -- Version 0.3.0 Active_Yeast
     -- created database and succesfully established all databases
'''

dialect = 'postgresql'
username = 'postgres'
password='8949'
host = 'localhost:5432'
database_name = 'picco'

database_path = f'{dialect}://{username}:{password}@{host}/{database_name}'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    '''
    binds a flask application and a SQLAlchemy service
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    migrate = Migrate(app, db)


class Restaurant(db.Model):
    '''
    Restaurant

    Relationships:
     -- one to many relationship with [Order]
     -- one to one relationship with [Location]
    '''
    __tablename__ = 'restaurants'

    id =                    Column(Integer, primary_key=True)
    name =                  Column(String(150), nullable=False)
    phone =                 Column(String(50), nullable=False)
    location    =           db.relationship('Location', backref='restaurants', lazy=True)
    info    =               db.relationship('RestaurantInfo', backref='restaurants', lazy=True)
    menu_items =            db.relationship('Menu', backref='restaurants', lazy=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'name':self.name,
            'phone':self.phone,
        }

class Location(db.Model):
    __tablename__ = 'location'

    id =                        Column(Integer, primary_key=True)
    restaurant_id =             Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    address =                   Column(String, nullable=False)
    city =                      Column(String, nullable=False)
    zipcode =                   Column(Integer)
    state =                     Column(String, nullable=False)

    def __init__(self, restaurant_id, address, city, zipcode, state):
        self.restaurant_id = restaurant_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.state = state
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    89
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'restaurant_id':self.restaurant_id,
            'address':self.address,
            'city':self.city,
            'zipcode':self.zipcode,
            'state':self.state
        }

class RestaurantInfo(db.Model):
    __tablename__ = 'restaurantinfo'

    id =                        Column(Integer, primary_key=True)
    restaurant_id =             Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    website =                   Column(String(200))
    description =               Column(String)
    classification =            Column(String(100))
    yelp_link =                 Column(String(200))

    def __init__(self, restaurant_id, website, description, classification, yelp_link):
        self.restaurant_id = restaurant_id
        self.website = website
        self.description = description
        self.classification = classification
        self.yelp_link = yelp_link
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'restaurant_id':self.restaurant_id,
            'website':self.website,
            'description':self.description,
            'classification':self.classification,
            'yelp_link':self.yelp_link
        }

class Menu(db.Model):
    '''
    Menu

    Relationships:
     -- one to many with [MenuItems]
    
    Imp Info:
     -- tod_menu
      -- [1] indicates breakfast menu
      -- [5] indicates lunch menu
      -- [10] indicates dinner menu
      -- [50] indicates all of the above menu
    '''
    __tablename__ = 'menu'

    id =                        Column(Integer, primary_key=True)
    restaurant_id =             Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    tod_menu =                  Column(Integer, nullable=False)
    name =                      Column(String, nullable=False)
    menu_items =                db.relationship('MenuItems', backref='menu', lazy=True)

    def __init__(self, restaurant_id, tod_menu, name):
        self.restaurant_id = restaurant_id
        self.tod_menu = tod_menu
        self.name = name
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'restaurant_id':self.restaurant_id,
            'tod_menu':self.tod_menu,
            'name':self.name
        }

class MenuItems(db.Model):
    '''
    MenuItems
    '''
    __tablename__ = 'menuitems'

    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(400), nullable=False)
    price = Column(Float, nullable=False)
    order_item = db.relationship('OrderItems', backref='menuitems', lazy=True)

    def __init__(self, menu_id, name, description, price, order_item):
        self.menu_id = menu_id
        self.name = name
        self.description = description
        self.price = price
        self.order_item = order_item
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'menu_id':self.menu_id,
            'name':self.name,
            'description':self.description,
            'price':self.price,
            'order_item':self.order_item
        }

class Order(db.Model):
    '''
    Order

    Relationships:
     -- one to many relationship with [OrderStatus]
     -- one to one relationship with [OrderItems]

    Imp Info:
     -- each row indicates order. Historical log in [OrderStatus]. Gen order info in [OrderItems]
    '''
    __tablename__ = 'orders'

    id =                        Column(Integer, primary_key=True)
    restaurant_id =             Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    received_timestamp =        Column(TIMESTAMP, nullable=False)
    confirmation_timestamp =    Column(TIMESTAMP)
    complete_timestamp =        Column(TIMESTAMP)
    total_price =               Column(Float, default=0)
    order_status =              db.relationship('OrderStatus', backref='orders', lazy=True)
    order_items =               db.relationship('OrderItems', backref='orders', lazy=True)

    def __init__(self, restaurant_id, received_timestamp, confirmation_timestamp, complete_timestamp):
        self.restaurant_id = restaurant_id
        self.received_timestamp = received_timestamp
        self.confirmation_timestamp = confirmation_timestamp
        self.complete_timestamp = complete_timestamp

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'restaurant_id':self.restaurant_id,
            'received_timestamp':self.received_timestamp,
            'confirmation_timestamp':self.confirmation_timestamp,
            'complete_timestamp':self.complete_timestamp,
            'order_status':self.order_status,
            'order_items':self.order_items
        }

class OrderStatus(db.Model):
    '''
    OrderStatus

    Imp Info:
     -- state heirarchy:
         -- [1] received
         -- [5] confirmed
         -- [10] in_progress
         -- [15] checklist_verification
         -- [20] complete
     -- each row indicates a change in state (historical)
    '''
    __tablename__ = 'orderstatus'

    id =                    Column(Integer, primary_key=True)
    order_id =              Column(Integer, ForeignKey('orders.id'), nullable=False)
    state =                 Column(Integer, nullable=False)
    ts =                    Column(TIMESTAMP, nullable=False)

    def __init__(self, order_id, state, ts):
        self.order_id = order_id
        self.state = state
        self.ts = ts
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        {
            'id':self.id,
            'order_id':self.order_id,
            'state':self.state,
            'ts':self.ts
        }


class OrderItems(db.Model):
    '''
    OrderItems

    Relationships:
     -- one to one with [MenuItems]
    '''
    __tablename__ = 'orderitems'

    id =                        Column(Integer, primary_key=True)
    order_id =                  Column(Integer, ForeignKey('orders.id'), nullable=False)
    quantity =                  Column(Integer, default=1)
    menu_item =                 Column(Integer, ForeignKey('menuitems.id'), nullable=False)

    def __init__(self, order_id, item_id, quantity, menu_item):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity
        self.menu_item = menu_item
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'order_id':self.order_id,
            'quantity':self.quantity,
            'menu_item':self.menu_item
        }

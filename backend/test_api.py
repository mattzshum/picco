import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models import setup_db, Restaurant, Location, Menu, RestaurantInfo, Order, OrderItems, OrderStatus, MenuItems

# Unittests for Piccos APIs

# TODO:
'''
 -- Create unittests one by one
'''

# Changelog:
'''
 -- Version 0.1.0 Creator
     -- Init Creation
'''

class PiccoTestCases(unittest.TestCase):
    '''
    Class containing all API test cases for PICCO
    '''

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.dialect = 'postgresql'
        self.username = 'postgres'
        self.password='8949'
        self.host = 'localhost:5432'
        self.database_name = 'picco'
        self.database_path = f'{self.dialect}://{self.username}:{self.password}@{self.host}/{self.database_name}'

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        '''
        Executed after each test
        '''
        pass


    def test_insert_restaurant(self):
        '''
        Currently testing by inserting a John Doe Case
        '''
        ins_restaurant = Restaurant('John Doe', '5103388949')
        ins_restaurant.insert()
        restaurant_id = ins_restaurant.id
        # print(f'INSERTED: {restaurant_id}')
        ins_location = Location(restaurant_id=restaurant_id, address='1234 John Doe Ave', city='San Francisco', zipcode=94502, state='CA')
        ins_ri = RestaurantInfo(restaurant_id=restaurant_id, website='website.com', description='John Doe Bakery', classification='type_all', yelp_link='yelp.com/1')
        ins_location.insert()
        ins_ri.insert()

        res = self.client().get(f'/restaurants/{restaurant_id}')
        self.assertEqual(res.status_code, 200)

    def test_get_all_restaurants(self):
        '''
        Currently set to 404 because the database is not populated
        '''
        res = self.client().get('/restaurants')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['restaurants'], list)
    
    def test_get_specific_restaurant(self):
        ins_restaurant = Restaurant('John Doe', '5103388949')
        ins_restaurant.insert()
        restaurant_id = ins_restaurant.id
        # print(f'INSERTED: {restaurant_id}')
        ins_location = Location(restaurant_id=restaurant_id, address='1234 John Doe Ave', city='San Francisco', zipcode=94502, state='CA')
        ins_ri = RestaurantInfo(restaurant_id=restaurant_id, website='website.com', description='John Doe Bakery', classification='type_all', yelp_link='yelp.com/1')
        ins_location.insert()
        ins_ri.insert()

        res = self.client().get(f'/restaurants/{restaurant_id}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['data'], dict)
    
    def test_delete_restaurant(self):
        '''
        removes all instances of the above created restaurant objects
        includes: [restaurant, location, restaurant_info]
        '''
        ins_restaurant = Restaurant('John Doe', '5103388949')
        ins_restaurant.insert()
        restaurant_id = ins_restaurant.id
        print(f'INSERTED for DELETION: {restaurant_id}')
        ins_location = Location(restaurant_id=restaurant_id, address='1234 John Doe Ave', city='San Francisco', zipcode=94502, state='CA')
        ins_ri = RestaurantInfo(restaurant_id=restaurant_id, website='DELETION', description='John Doe Bakery', classification='type_all', yelp_link='yelp.com/1')
        ins_location.insert()
        ins_ri.insert()

        print(ins_ri)

        res = self.client().delete(f'/restaurants/{restaurant_id}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()
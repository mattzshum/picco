import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models import setup_db, Restaurant, Location, Menu, RestaurantInfo, Order, OrderItems, OrderStatus, MenuItems

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

    def test_get_all_restaurants(self):
        res = self.client().get('/restaurants')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(data['restaurants'], list)

if __name__ == '__main__':
    unittest.main()
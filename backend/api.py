import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc 
import json
from flask_cors import CORS
import babel
from datetime import dateutil

from .models import setup_db, Restaurant, Location, Menu, RestaurantInfo, Order, OrderItems, OrderStatus, MenuItems
# from auth.auth import AuthError, requires_auth -> to be implemented after auth0 implementation

RESTAURANTS_PER_PAGE = 10


def format_datetime(value, format='medium'):
    '''
    function that formats datetime fo the proper format
    '''
    date = dateutil.parser.parse(value)
    if format == 'full':
        format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)

def paginate_restaurants(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * RESTAURANTS_PER_PAGE
    end = start + RESTAURANTS_PER_PAGE

    restaurants = [restaurant.format() for restaurant in selection]
    current_restaurants = restaurants[start:end]
    return current_restaurants

def create_app(test_config=None):
    '''
    Home of the API logics
    '''
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/restaurants', methods=['GET'])
    def restaurants():
        restaurants = Restaurant.query.order_by(Restaurant.id).all()
        current_restaurants = paginate_restaurants(request, restaurants)

        if len(current_restaurants == 0):
            abort(404)
        
        return jsonify({
            'success':True,
            'restaurants':[restaurant.format() for restaurant in current_restaurants],
            'total_restaurants':len(Restaurant.query.all()),
        })
    
    @app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
    def specific_restaurant(restaurant_id):
        try:
            restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
            location = Location.query.filter(Location.restaurant_id == restaurant_id).one_or_none()
            current_menus = Menu.query.filter(Menu.restaurant_id == restaurant_id).all()
            restaurant_info = RestaurantInfo.query.filter(RestaurantInfo.restaurant_id == restaurant_id).one_or_none()

            if restaurant is None:
                abort(404)
            
            return jsonify({
                'success':True,
                'data':restaurant.format(),
                'location':location.format(),
                'menus':[menu.format() for menu in current_menus],
                'restaurant_gen_info':restaurant_info.format()
            })
    
    @app.route('/restaurants/search', methods=['POST'])
    def search_restaurants(search_term):
        search_term = request.json.get('search_term', '')
        restaurants = Restaurant.query.order_by(Restaurant.id).filter(
                        Restaurant.name.ilike(f'%{search_term}%') )
        current_restaurants = paginate_restaurants(request, restaurants)

        if restaurants is None:
            abort(404)
        
        return jsonify({
            'success':True,
            'restaurants':[restaurant.format() for restaurant in current_restaurants],
            'total_restaurants':len(restaurants)
        })

    @app.route('/restaurants', methods=['POST'])
    def create_restaurant():
        body = request.get_json()

        # - PARTITION Restaurant
        new_name = body.get('name', None)
        new_phone = body.get('phone', None)
        # - PARTITION Location
        new_address = body.get('address', None)
        new_city = body.get('city', None)
        new_zipcode = body.get('zipcode', None)
        new_state = body.get('state', None)
        # - PARTITION RestaurantInfo
        new_website = body.get('website', None)
        new_description = body.get('description', None)
        new_classification = body.get('classification', None)
        new_yelp_link = body.get('yelp_link', None)

        try:
            restaurant = Restaurant(name=new_name, phone=new_phone)
            Restaurant.insert(restaurant)

            location = Location(restaurant_id=restaurant.id, address=new_address, city=new_city, zipcode=new_zipcode, state=new_state)
            Location.insert(location)

            restaurant_info = RestaurantInfo(restaurant_id=restaurant.id, website=new_website, description=new_description, classification=new_classification, yelp_link=new_yelp_link)
            RestaurantInfo.insert(restaurant_info)

            # just need to return restaurant.id for redirect on proper creation
            return jsonify({
                'success':True,
                'created':restaurant.id
            })
        except Exception as E:
            abort(422)
    
    @app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
    def delete_restaurant(restaurant_id):
        target_restaurant = Restaurant.query.filter(Restaurant.id==restaurant_id).one_or_none()
        try:
            if target_restaurant is None:
                abort(404)
            
            target_restaurant.delete()

            return jsonify({
                'success':True,
                'deleted':restaurant_id
            })
        except Exception as E:
            abort(422)

    @app.route('/restaurants/<int:restaurant_id>/edit', methods=['PATCH'])
    def edit_restaurant(restaurant_id):
        target_restaurant = Restaurant.query.get(restaurant_id)
        target_location = Location.query.filter(Location.restaurant_id == restaurant_id).one_or_none()
        target_restaurantinfo = RestaurantInfo.query.filter(Restaurant.restaurant_id == restaurant_id).one_or_none()

        if target_restaurant is None or target_location is None or target_restaurantinfo is None:
            abort(404)

        body = request.get_json()

        try:
            # - PARTITION Restaurant
            target_restaurant.name = body.get('name', None)
            targer_restaurant.phone = body.get('phone', None)
            # - PARTITION Location
            target_location.address = body.get('address', None)
            target_location.city = body.get('city', None)
            target_location.zipcode = body.get('zipcode', None)
            target_location.state = body.get('state', None)
            # - PARTITION RestaurantInfo
            target_restaurantinfo.website = body.get('website', None)
            target_restaurantinfo.description = body.get('description', None)
            target_restaurantinfo.classification = body.get('classification', None)
            target_restaurantinfo.yelp_link = body.get('yelp_link', None)

            target_restaurant.update()
            target_location.update()
            target_restaurantinfo.update()

            return jsonify({
                'success':True,
                'updated':restaurant_id
            })
        except Exception as E:
            abort(422)
    
    @app.route('/restaurants/<int:restaurant_id>/menus', methods=['GET'])
    def menus(restaurant_id):
        current_menus = Menu.query.filter(Menu.restaurant_id == restaurant_id).all()

        if current_menus is None:
            abort(404)
        
        return jsonify({
            'success':True,
            'menus':[menu.format() for menu in current_menus]
        })

    @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>', methods=['GET'])
    def specific_menu(restaurant_id, menu_id):
        menu = Menu.query.filter(Menu.restaurant_id == restaurant_id). \
                          filter(Menu.id == menu_id).all()
        menu_items = MenuItems.query.filter(MenuItems.menu_id == menu_id)

        if menu is None:
            abort(404)
        
        return ({
            'success':True,
            'menu':menu.format(),
            'menu_items':[menu_item.format() for menu_item in menu_items]
        })


    @app.route('/restaurants/<int:restaurant_id>/menus', methods=['POST'])
    def create_menu(restaurant_id):
        body = request.get_json()

        new_tod_menu = body.get('tod_menu', None)
        new_name = body.get('name', None)
        try:
            menu = Menu(tod_menu=new_tod_menu, name=new_name)
            Menu.insert(menu)

            return jsonify({
                'success':True,
                'created':menu.id
            })

    @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['PATCH'])
    def edit_menu(restaurant_id, menu_id):
        target_menu = Menu.query.filter(Menu.restaurant_id == restaurant_id). \
                                 filter(Menu.menu_id == menu_id)
        body = request.get_json()

        try:
            target_menu.tod_menu = body.get('tod_menu', None)
            target_menu.name = body.get('name', None)

            target_menu.update()

            return jsonify({
                'success':True,
                'updated':menu_id
            })
        except Exception as E:
            abort(422)
    
    @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>', methods=['DELETE'])
    def delete_menu(restaurant_id, menu_id):
        target_menu = Menu.query.filter(Menu.restaurant_id == restaurant_id). \
                                 filter(Menu.id == menu_id)
        if target_menu is None:
            abort(404)

        try:
            target_menu.delete()

            return jsonify({
                'success':True,
                'deleted':menu_id
            })
        except Exception as E:
            abort(422)

    @app.route('/restaurants/<int:restaurant_id>/orders', methods=['GET'])
    def orders(restaurant_id):
        '''
        restaurant side order screen

        NOTE: We do not want to paginate this screen for now
        '''
        current_orders = Order.query.filter(Order.restaurant_id == restaurant_id).all()
        
        if current_orders is None:
            abort(404)
        
        return ({
            'success':True,
            'orders':[order.format() for order in current_orders]
        })

    @app.route('/restaurants/<int:restaurant_id>/<int:order_id>', methods=['GET'])
    def specific_order(restaurant_id, order_id):
        '''
        restaurant side order screen

        NOTE: in future, only restaurant has access to this. users will have own API for specific order
        '''
        order = Order.query.filter(Order.restaurant_id == restaurant_id). \
                            filter(Order.id == order_id)
        
        if order is None:
            abort(404)
        
        return jsonify({
            'success':True,
            'order':order.format()
        })
    
    # @app.route('/restaurants/<int:restaurant_id>', methods=['POST'])
    # def create_order(restaurant_id):
    #     request = body.get_json()

    #     new_received_timestamp = datetime.now()
    #     new_total_price

    @app.errorhandler(404)
    def not_fount(error):
        return jsonify({
            'success':False,
            'error':404,
            'message':'Not Found'
        }), 404
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':422,
            'message':'Not Processable'
        }), 422
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success':False,
            'error':500,
            'message':'Server Error'
        }), 500

    return app
    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Headers',
    #                          'Content-Type,Authorization,true')
    #     response.headers.add('Access-Control-Allow-Headers',
    #                          'GET,PATCH,POST,DELETE,OPTIONS')
    #     return response
import React, { useState, useEffect } from "react";
import "../stylesheets/Restaurant.css"
import RestaurantCard from './RestaurantCard'

const Restaurant = () => {

    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        console.log('fetching restaurants');
        getRestaurants();
    }, []);

    const getRestaurants = async () => {
        const response = await fetch('http://127.0.0.1:5000/restaurants').then(res => res.json());
        console.log(response)
        // console.log(response.restaurants)
        setRestaurants(response.restaurants);
    }

    return(
        <div>
            <div className='restaurants'>
                <h2>Restaurant</h2>
                {restaurants && restaurants.map(restaurant =>(
                    <RestaurantCard
                      key={restaurant.id}
                      name={restaurant.name}
                      phone={restaurant.phone} />
                ))}
            </div>
        </div>
    )
}

export default Restaurant;
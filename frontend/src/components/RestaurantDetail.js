import React, { useState, useEffect } from 'react';
// import './App.css' 

function RestaurantDetail({ match }) {
    useEffect(() => {
        console.log('fetching restaurant details')
        fetchRestaurantDetails();
        console.log(match)
    }, []);

    const [restaurantDetail, setRestaurantDetail] = useState({});

    const fetchRestaurantDetails = async () => {
        const response = await fetch('http://127.0.0.1:5000/restaurants/1').then(res => res.json());
        console.log(response)
    }

    return (
        <div>
            <p>{}</p>
        </div>
    )
}

export default RestaurantDetail;
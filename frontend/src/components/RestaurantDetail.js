import React, { useState, useEffect } from 'react';
import '../stylesheets/RestaurantDetail.css' 
import LocationPanel from './LocationPanel'
import ExternalLinkPanel from './ExternalLinkPanel'

function RestaurantDetail({ match }) {
    useEffect(() => {
        console.log('fetching restaurant details')
        fetchRestaurantDetails();
        // console.log(match)
    }, []);

    const [restaurantData, setRestaurantData] = useState({});
    const [restaurantLocation, setRestaurantLocation] = useState({});
    const [restaurantGenInfo, setRestaurantGenInfo] = useState({});

    const fetchRestaurantDetails = async () => {
        const response = await fetch(`http://127.0.0.1:5000/restaurants/${match.params.id}`).then(res => res.json());
        console.log(response)
        setRestaurantData(response.data)
        setRestaurantLocation(response.location)
        setRestaurantGenInfo(response.restaurant_gen_info)
        /*dev logs
        console.log(response.data)
        console.log(response.location)
        console.log(response.restaurant_gen_info)
        */
    }

    return (
        <div>
            <div className='name'>
                <h2>{restaurantData.name}</h2>
                <p class='description'>{restaurantGenInfo.description}</p>
            </div>
            <div className='gen-info'>
                <LocationPanel
                    address={restaurantLocation.address}
                    state={restaurantLocation.state}
                    zipcode={restaurantLocation.zipcode}
                    phone={restaurantData.phone}
                />
            </div>
            <div className='external-links'>
                <ExternalLinkPanel
                    website={restaurantGenInfo.website}
                    yelp_link={restaurantGenInfo.yelp_link}
                />
            </div>
        </div>
    )
}

export default RestaurantDetail;
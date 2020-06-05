import React, { useState, useEffect } from 'react';
import "../stylesheets/RestaurantCard.css"
import {Link} from 'react-router-dom';

const RestaurantCard = ({id, name, phone}) => {
    return (
        <div>
            <h3>ID: {id}</h3>
            <Link to={`/restaurants/${id}`}>{name}</Link>
            <p class='contact-info'>Phone Number: {phone}</p>
        </div>
    )
}

export default RestaurantCard;
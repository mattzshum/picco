import React, { useState, useEffect } from 'react';
import "../stylesheets/RestaurantCard.css"
import {Link} from 'react-router-dom';

const RestaurantCard = ({id, name, phone}) => {

    useEffect(() => {
        console.log(id, name, phone);
    }, []);

    return (
        <div class='container'>
            <div class='card'>
                <div class='contentBx'>
                    <Link to={`/restaurants/${id}`} class='name'>{name}</Link>
                </div>
                <div class='phone'>
                    <span>{phone}</span>
                </div>
            </div>
        </div>
    )
}

export default RestaurantCard;
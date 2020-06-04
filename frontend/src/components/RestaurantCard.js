import React, { useState, useEffect } from 'react';
import "../stylesheets/RestaurantCard.css"

const RestaurantCard = ({id, name, phone}) => {
    return (
        <div>
            <h3>{name}</h3>
            <p>{phone}</p>
        </div>
    )
}

export default RestaurantCard;
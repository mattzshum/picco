import React from "react";
import "../stylesheets/Restaurant.css"

const Restaurant = ({name, phone}) => {
    return(
        <div className="restaurant">
            <h3>{name}</h3>
            <p>{phone}</p>
        </div>
    )
}

export default Restaurant;
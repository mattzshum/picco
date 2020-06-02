import React from "react";
import "./stylesheets/App.css"

function Restaurant(props){
    return(
        <div className="restaurant">
            <h3>{props.name}</h3>
            <p>{props.location}</p>
        </div>
    )
}
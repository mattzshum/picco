import React, { useEffect } from 'react';
import '../stylesheets/LocationPanel.css'

const LocationPanel = ({address, state, zipcode, phone}) => {
    useEffect(() =>{
        console.log(address, state, zipcode, phone)
    }, []);

    return (
        <div class='loc-container'>
            <div class='loc-card'>
                <div class='loc-contentBx'>
                    <h3>Contact info</h3>
                    <ul class='info'>
                        <li>{address}, {state}, {zipcode}</li>
                        <li>{phone}</li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default LocationPanel;
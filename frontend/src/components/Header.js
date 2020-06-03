import React, { Component } from 'react';
import '../stylesheets/Header.css';

class Header extends Component {
    render() {
        return (
            <div>
                <div class='logo-container'>
                    <img src="./img/logo.svg" alt='logo' />
                    <h4 class='logo'>Picco</h4> 
                </div>
                <nav>
                    <ul class='nav-links'>
                        <li><a class='nav-link' href='#'>Restaurants</a></li>
                        <li><a class='nav-link' href='#'>Locations</a></li>
                        <li><a class='nav-link' href='#'>Orders</a></li>
                    </ul>
                </nav>
                <div class='cart'>
                    <img src='./img/cart.svg' alt='cart' />
                </div>
            </div>
        )
    }
}

export default Header;
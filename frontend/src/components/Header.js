import React, { Component } from 'react';
import '../stylesheets/Header.css';
import {Link} from 'react-router-dom';

class Header extends Component {
    render() {
        return (
            <div>
                <div className='logo-container'>
                    {/* <img src="./img/logo.svg" alt='logo' /> */}
                    <Link to='/' style={{ textDecoration: 'none'}}> <h4 className='logo'>Picco</h4> </Link>
                </div>
                <nav>
                    <ul class='nav-links'>
                        <Link to='/restaurants' style={{ textDecoration: 'none'}}> <li><a class='nav-link'>Restaurants</a></li> </Link>
                        <Link to='/locations' style={{ textDecoration: 'none'}}> <li><a class='nav-link'>Locations</a></li> </Link>
                        <Link to='/orders' style={{ textDecoration: 'none'}}> <li><a class='nav-link' >Orders</a></li> </Link>
                    </ul>
                </nav>
                {/* <div class='cart'>
                    <img src='./img/cart.svg' alt='cart' />
                </div> */}
            </div>
        )
    }
}

export default Header;
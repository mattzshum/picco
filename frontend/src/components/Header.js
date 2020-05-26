import React, { Component } from 'react';
import '../stylesheets/Header.css';

class Header extends Component {
    navTo(uri){
        window.location.href = window.location.origin + uri;
    }

    render() {
        return (
            <div className='App-header'>
                <h1 onClick={() => {this.navTo('')}}>Picco</h1>
                <h2 onClick={() => {this.navTo('/restaurants')}}>Restaurant</h2>
            </div>
        )
    }
}

export default Header;
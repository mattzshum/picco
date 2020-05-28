import React, {Component} from 'react';

import '../stylesheets/App.css';
import '../stylesheets/Restaurant.css';
import $ from 'jquery';

class Restaurant extends Component{
    constructor(){
        super();
        this.state = {
            restaurants: [],
            page: 1,
            total_restaurants: 0,
        }
    }
    componentDidMount(){
        this.getRestaurants();
    }

    getRestaurants = () => {
        $.ajax({
            url: `/restaurants?page=${this.state.page}`,
            type: "GET",
            success: (result) => {
                this.setState({
                    restaurants: result.restaurants,
                    total_restaurants: result.total_restaurants })
                return;
            },
            error: (error) => {
                alert('Unable to load restaurants. Please try your request again')
                return;
            }
        })
    }

    selectPage(num){
        this.setState({page: num}, () => this.getRestaurants())
    }

    render(){
        return (
            <div className="restaurant">
                <div className="restaurant-list">
                    <h2 onClick={() => {this.getRestaurants()}}>Restaurants</h2>
                    <ul>
                        {this.state.restaurants}
                    </ul>
                </div>
            </div>
        )
    }
}

export default Restaurant;
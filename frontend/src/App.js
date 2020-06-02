import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';

import './stylesheets/App.css';
import Header from './components/Header'
import Restaurant from './components/Restaurant';
import Restaurant from './rest_test'

function App{
  const [restaurants, setRestaurants] =([
      { name: 'Ed', location: '1234 john doe ave'}
  ])
  return (
      <div className="restaurant">
          <form className='search-form'>
            <input className='search-bar' type='text' />
            <button className='search-button' type='submit'> Search </button>
          </form>
          {restaurants.map(restaurant =>(
            <Restaurant name={restaurant.name} location={restaurant.location} />
          ))}
      </div>
  )
}

export default App;


/*

// useEffect() is a function that runs the first time an app is run
useEffect(() => {
  getRestaurants();
}; []);

// This is the API call that we can experiment with. Use to talk with local Test DB for now
const getRestaurants = async () => {
  const response = await fetch('localhost:5000/restaurants);
  const data = await response.json(); // NOTE do you need to json here? API already returns json object
  console.log(data);
}
*/
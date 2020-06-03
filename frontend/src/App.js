import React, { useState, useEffect } from 'react';
// import {
//   BrowserRouter as Router,
//   Route,
//   Switch
// } from 'react-router-dom';

import './stylesheets/App.css';
import Header from './components/Header'
import Restaurant from './components/Restaurant';

const App = () => { 

  // const [restaurants, setRestaurants] =([
  //     { name: 'Ed', location: '1234 john doe ave'}
  // ])
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    console.log('getting restaurants');
    getRestaurants();
  }, []);

  const getRestaurants = async () => {
    const response = await fetch('http://127.0.0.1:5000/restaurants').then(res => res.json());
    console.log(response.restaurants);
    setRestaurants(response.restaurants)
    // const data = await response.json(); // NOTE do you need to json here? API already returns json object
  }

  return (
      <div className="App">
        <Header />
          <form className='search-form'>
            <input className='search-bar' type='text' />
            <button className='search-button' type='submit'> Search </button>
          </form>

          <div className='restaurants'>
            {restaurants && restaurants.map(restaurant =>(
              <Restaurant
                key={restaurant.id} 
                name={restaurant.name}
                phone={restaurant.phone}/>
            ))}
          </div>
      </div>
  )
}

export default App;


/*

import {Link} from 'react-router-dom';

// import {
//   BrowserRouter as Router,
//   Route,
//   Switch
// } from 'react-router-dom';

<Link to='/about'

<Router>
<Switch>
<Route path='/' component={Home} />
<Route path='/restaurants'  component={Restaurant} />
<Route path='/locations' component={Location} />
<Route path='/orders' component={Orders} />
</Switch>
</Router>

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
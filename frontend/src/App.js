import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';

import './stylesheets/App.css';
import Header from './components/Header'
import Restaurant from './components/Restaurant';
import Location from './components/Location';
import Order from './components/Order';
import RestaurandDetail from './components/RestaurantDetail'

const App = () => { 

  return (
      <div className="App">
        <Router>
          <Header />
          <Switch>
            {/* <Route path='/' exact component={Home} /> */}
            <Route path='/restaurants' exact component={Restaurant} />
            <Route path='/locations' exact component={Location} />
            <Route path='/orders' exact component={Order} />
            <Route path='/restaurants/:id>' component={RestaurandDetail} />
          </Switch>
        </Router>
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

<Link to='/about' exact />

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
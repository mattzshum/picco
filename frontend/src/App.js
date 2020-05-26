import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';

import './stylesheets/App.css';
import Header from './components/Header'
import Restaurant from './components/Restaurant';

class App extends Component {
  render(){
    return (
      <div className="App">
        <Header path />
        <Router>
          <Switch>
            <Route path='/' exact component={Restaurant} />
          </Switch>
        </Router>
      </div>
    )
  }
}

export default App;
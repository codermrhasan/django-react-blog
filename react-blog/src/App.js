import React, { Component } from 'react';
import {Provider} from 'react-redux';
import {Route, Switch, BrowserRouter} from 'react-router-dom';

import Blog from './components/index';
import NotFound from './components/NotFound';
import './App.css';
import store from './redux/store/index';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
      <BrowserRouter>
      <div className="App">
        <Switch>
          <Route exact path="/" component={Blog} />
          <Route component={NotFound} />
        </Switch>
      </div>
      </BrowserRouter>
      </Provider>
    )
  }
}


export default App
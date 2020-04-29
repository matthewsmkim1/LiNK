import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import history from "../history";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

import LoginForm from "./auth/Login";
import RegistrationForm from "./auth/Registration";

const DashBoard = (props) => {
  return (
    <div>
      <h1>Index links</h1>
      <p>
        <a href="/login">Login</a>
        {"\n"}
        <a href="/register">Register</a>
      </p>
    </div>
  );
};

class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
  }

  render() {
    return (
      <Provider store={store}>
        <Router history={history}>
          <Switch>
            {/* <PrivateRoute exact path="/" component={DashBoard} /> */}
            <Route exact path="/" component={DashBoard} />
            <Route exact path="/register" component={RegistrationForm} />
            <Route exact path="/login" component={LoginForm} />
          </Switch>
        </Router>
      </Provider>
    );
  }
}

export default App;

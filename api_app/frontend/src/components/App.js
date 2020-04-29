import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import history from "../history";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

import LoginForm from "./auth/Login";
import RegistrationForm from "./auth/Registration";
import TopBar from "./layout/TopBar";
import Entries from "./layout/Entries";
import GroupEntries from "./layout/GroupEnrties";
import ViewGroup from "./layout/ViewGroups";

const DashBoardSimple = (props) => {
  return (
    <div>
      <h1>Index links</h1>
      <p>
        <a href="/login">Login</a>
        {"\n"}....
        <a href="/register">Register</a>
        {"\n"}....
        <a href="/new">New Component</a>
        {"\n"}....
        <a href="/dashy">Entries</a>
        {"\n"}....
        <a href="/view-group">view groups</a>
        {"\n"}....
        <a href="/group-entries">group posts</a>
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
            <Route exact path="/" component={DashBoardSimple} />
            <Route exact path="/register" component={RegistrationForm} />
            <Route exact path="/login" component={LoginForm} />
            <Route exact path="/new" component={TopBar} />
            <Route exact path="/dashy" component={Entries} />
            <Route exact path="/view-group" component={ViewGroup} />
            <Route exact path="/group-entries" component={GroupEntries} />
          </Switch>
        </Router>
      </Provider>
    );
  }
}

export default App;

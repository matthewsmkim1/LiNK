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
import CreateEntry from "./post_forms/CreateEntry";
// import JoinGroup from "./group_forms/JoinGroup";
// import CreateGroup from "./group_forms/CreateGroup";

const DashBoardSimple = (props) => {
  return (
    <div>
      <h1>Index links</h1>
      <p>
        <h2>
          <a href="/login">Login</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/register">Register</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/new">New Component</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/dashy">Entries</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/view-group">view groups</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/group-entries">group posts</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/create-post">create-post</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/create-group">create-group</a>
          {"\n"}....
        </h2>
        <h2>
          <a href="/join-group">join-group</a>
          {"\n"}....
        </h2>
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
      <React.Fragment>
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
            <Route exact path="/create-post" component={CreateEntry} />
            {/* <Route exact path="/create-group" component={CreateGroup} />
            <Route exact path="/join-group" component={JoinGroup} /> */}
          </Switch>
        </Router>
      </Provider>
      <div>
        hello
      </div>

      </React.Fragment>
    );
  }
}

export default App;

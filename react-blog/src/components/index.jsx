import React, { Component } from "react";
import { connect } from "react-redux";

import { getProfileFetch, logoutUser } from "../redux/actions";
import Login from "./Login";
import Register from "./Register";
import PostList from './PostList';
import {allPostFetch} from '../redux/actions/index'

class Blog extends Component {
  componentDidMount = () => {
    this.props.getProfileFetch();
  };
  logoutHandleClick = event => {
      event.preventDefault()
      localStorage.removeItem("token")
      this.props.logoutUser()
  }

  render() {
    let Nav = <nav></nav>;
    let Main = <main><Register/></main>
    let Aside = <aside><Login/></aside>
    if (localStorage.token) {
      Nav = (
        <nav>
          <ul>
            <li>
              <a href='/' >Home</a>
            </li>
            <li>
              <a href="#">My Page</a>
            </li>
            <li>
              <a href="#" onClick={this.logoutHandleClick}>LogOut</a>
            </li>
          </ul>
        </nav>
        
      );
      Main = (
          <main>
                <PostList/>
          </main>
      );
      Aside = (
          <aside>
              You're Logged In
          </aside>
      );
    }
    return (
      <React.Fragment>
        <header>
          <h1>React Blog App</h1>
        </header>
        {Nav}
        {Main}
        {Aside}
        
      </React.Fragment>
    );
  }
}
const mapStateToProps = state => {
  return {
    currentUser: state.authReducer.currentUser
  };
};

const mapDispatchToProps = dispatch => ({
  getProfileFetch: () => dispatch(getProfileFetch()),
  logoutUser: () => dispatch(logoutUser()),
  allPostFetch: () => dispatch(allPostFetch())
});

export default connect(mapStateToProps, mapDispatchToProps)(Blog);

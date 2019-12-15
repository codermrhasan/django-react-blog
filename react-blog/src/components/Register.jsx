import React, { Component } from "react";
import { connect } from "react-redux";

import { userPostFetch } from "../redux/actions";
import "./css/register.css";

class Register extends Component {
  state = {
    username: "",
    password: "",
    first_name: "",
    last_name: ""
  };
  
  handleChange = event => {
    this.setState({
      [event.target.name]: event.target.value
    });
  };

  handleSubmit = event => {
    event.preventDefault();
    this.props.userPostFetch(this.state);
    this.resetForm();
  };

  render() {
    return (
      <form className="registration-form" onSubmit={this.handleSubmit}>
        <fieldset>
          <legend>Sign Up</legend>
          <p>
            <label>Username</label>
            <input
              name="username"
              placeholder="Username"
              value={this.state.username}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={this.state.password}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <label>First Name</label>
            <input
              name="first_name"
              placeholder="First Name"
              value={this.state.first_name}
              onChange={this.handleChange}
            />
          </p>
          <p>
            <label>Last Name</label>
            <input
              name="last_name"
              placeholder="Last Name"
              value={this.state.last_name}
              onChange={this.handleChange}
            />
          </p>
          <p>
            <button type="submit">SignUp</button>
          </p>
        </fieldset>
      </form>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  userPostFetch: userInfo => dispatch(userPostFetch(userInfo))
});

export default connect(null, mapDispatchToProps)(Register);

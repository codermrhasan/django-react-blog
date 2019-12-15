import React, {Component} from "react";
import {connect} from "react-redux";

import {userLoginFetch} from "../redux/actions";

import './css/login.css';


class Login extends Component {
    state = {
        username: "",
        password: "",
    }
    handleChange = event => {
        this.setState({
          [event.target.name]: event.target.value
        });
      }
    handleSubmit = event => {
        event.preventDefault()
        this.props.userLoginFetch(this.state)
    }
    render(){
        return (
            <form className='login-form' onSubmit={this.handleSubmit}>
                <fieldset>
                    <legend>LogIn</legend>
                    <p>
                        <input
                            type="text" name="username"
                            placeholder="username"
                            onChange={this.handleChange}
                            value = {this.state.uesrname} 
                        />
                    </p>
                    <p>
                        <input
                            type="password" name="password"
                            placeholder="password"
                            
                            onChange={this.handleChange} />
                    </p>
                    <p>
                        <button type="submit">Login</button>
                    </p>
                </fieldset>
            </form>
        );
    }
}

const mapDispatchToProps = dispatch => ({
    userLoginFetch: userInfo => dispatch(userLoginFetch(userInfo))
})

export default connect(null, mapDispatchToProps)(Login);

import { rootApiUrl } from "../constants/url";
import {LOGIN_USER, LOGOUT_USER} from '../constants/actionTypes';


const loginUser = userObj => ({
  type: LOGIN_USER,
  payload: userObj
});

export const logoutUser = () => ({
  type: LOGOUT_USER
})

export const userPostFetch = user => {
  return dispatch => {
    return fetch(`${rootApiUrl}/api/v1/register/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      },
      body: JSON.stringify(user)
    }).then(resp => {
      if (resp.status >= 300) {
        window.alert(`Error!: ${resp.status}`);
      } else if (resp.status >= 200) {
        window.alert("registration successfull. Please Login");
      }
      return resp.json();
    })
  };
};


export const userLoginFetch = user => {
  return dispatch => {
    return fetch(`${rootApiUrl}/api/v1/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      },
      body: JSON.stringify(user)
    })
      .then(resp => {
        if (resp.status >= 300) {
          console.log(`Error!: ${resp.status}`);
        } else if (resp.status >= 200) {
          console.log("Login Success");
        }
        return resp.json();
      })
      .then(data => {
        if (data.token) {
            localStorage.setItem("token", data.token);
            dispatch(loginUser(data.user));
            //   window.alert('Unable to log in with provided credentials.')
        } else if(data.non_field_errors) {
            window.alert('Unable to log in with provided credentials.')          
        }
      });
  };
};


export const getProfileFetch = () => {
    return dispatch => {
      const token = localStorage.token;
      if (token) {
        return fetch(`${rootApiUrl}/api/v1/account/`, {
          method: "GET",
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
            'Authorization': `Token ${token}`
          }
        })
          .then(resp => {
              return resp.json()
            })
          .then(data => {
            if (data.message) {
                
                // An error will occur if the token is invalid.
                // If this happens, you may want to remove the invalid token.
                localStorage.removeItem("token")
            } else {
              dispatch(loginUser(data))
            }
          })
      }
    }
  }
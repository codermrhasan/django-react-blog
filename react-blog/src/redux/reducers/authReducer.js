import {LOGIN_USER, LOGOUT_USER} from '../constants/actionTypes';

const initialState = {
  currentUser: {}
};

export default function authReducer(state = initialState, action) {
  switch (action.type) {
    case LOGIN_USER:
      return { ...state, currentUser: action.payload };
    case LOGOUT_USER:
      return {...state, currentUser: {}}
    default:
      return state;
  }
}

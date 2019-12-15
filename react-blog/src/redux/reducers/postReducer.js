import {FETCH_POST} from '../constants/actionTypes';


const initialState = {
    posts: []
}

export default function postReducer(state = initialState, action){
    switch (action.type){
        case FETCH_POST:        
            return {...state, posts: action.payload}
        default:
            return state;
    }
}
import { rootApiUrl } from "../constants/url";
import { FETCH_POST } from "../constants/actionTypes";

export const allPostFetch = () => {
  return dispatch => {
    return fetch(`${rootApiUrl}/api/v1/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      }
    })
      .then(resp => {
        return resp.json();
      })
      .then(posts => {
        dispatch({
          type: FETCH_POST,
          payload: posts
        });
      });
  };
};

export const createPostFetch = post => {
  return dispatch => {
    return fetch(`${rootApiUrl}/api/v1/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: `Token ${localStorage.token}`
      },
      body: JSON.stringify(post)
    })
      .then(resp => {
        if (resp.status >= 300) {
          window.alert(`Error!: ${resp.status}`);
        } else if (resp.status >= 200) {
          console.log("post succeed");
        }
        return resp.json();
      })
  };
};

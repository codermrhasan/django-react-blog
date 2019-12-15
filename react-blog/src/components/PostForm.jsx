import React, { Component } from "react";
import {connect} from 'react-redux';
import './css/postForm.css';
import {createPostFetch} from '../redux/actions/index'
class PostForm extends Component {
  state = {
    title: "",
    body: ""
  };

  resetForm = () => {
    this.setState({
        title: "",
        body: ""
    });
  };
  handleChange = event => {
    this.setState({
      [event.target.name]: event.target.value
    })
  };
  handleSubmit = event => {
      event.preventDefault();
      this.props.createPostFetch(this.state);
      this.resetForm();
  }
  render() {
    return (
      <form className="post-form" onSubmit={this.handleSubmit}>
        <fieldset>
          <legend>Create Post</legend>
          <p>
            <input
              type="text"
              name="title"
              placeholder="This Is Title"
              value={this.state.title}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <textarea
              name="body"
              placeholder="This is post body"
              value={this.state.body}
              onChange={this.handleChange}
              required
            />
          </p>
          <p>
            <button 
              type="submit"
              onClick={this.handleClick}
              >Post</button>
          </p>
        </fieldset>
      </form>
    );
  }
}
const mapStateToProps = state => {
  return {
    posts: state.postReducer.posts
  };
};
const mapDispatchToProps = dispatch => ({
    createPostFetch: post => dispatch(createPostFetch(post)),
})

export default connect(mapStateToProps, mapDispatchToProps)(PostForm);

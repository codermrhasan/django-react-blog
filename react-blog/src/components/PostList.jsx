import React, { Component } from "react";
import { connect } from "react-redux";
import { allPostFetch } from "../redux/actions";
import PostForm from "./PostForm";


class PostList extends Component {
  render() {
    this.props.allPostFetch();
    let posts = this.props.posts;
    console.log('post list')
    return (
      <React.Fragment>
        <PostForm />
        <div className="post-list">
          {posts.map(post => (
            <div className="post-container" key={post.id}>
              <h3 className="post-title">{post.title}</h3>
              <div className="post-under-head">
              <p>Post by {post.authors_username}</p>
              </div>
              <p className="post-body">
                {post.body}
              </p>
              <p className="post-footer">{post.total_comments} Comments</p>
            </div>
          ))}
        </div>
      </React.Fragment>
    );
  }
}

const mapStateToProps = state => {
  return {
    posts: state.postReducer.posts,
    currentUser: state.authReducer.currentUser
  };
};
const mapDispatchToProps = dispatch => ({
  allPostFetch: () => dispatch(allPostFetch())
});

export default connect(mapStateToProps, mapDispatchToProps)(PostList);

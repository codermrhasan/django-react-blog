from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)



from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/my_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.filter(author__id=self.kwargs['pk'])
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = comments
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/post_update.html'
    form_class = PostForm
    login_url = reverse_lazy('login')
    
    def get_object(self):
        id = self.kwargs.get('pk')
        post = Post.objects.get(id=id)
        if not self.request.user == post.author:
            raise PermissionDenied
        else: 
            return post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_object(self):
        id = self.kwargs.get('pk')
        post = Post.objects.get(id=id)
        if not self.request.user == post.author:
            raise PermissionDenied
        else: 
            return post

    def get_success_url(self):
        return reverse_lazy('posts', kwargs={'pk': self.request.user.id})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/comment_create.html'
    form_class = CommentForm
    login_url = reverse_lazy('login')
    success_url = '../'    

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        form.instance.post = Post.objects.get(id=id)
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/comment_confirm_delete.html'
    context_object_name = 'comment'
    login_url = reverse_lazy('login')
    success_url = '../../../' 

    def get_object(self):
        id = self.kwargs.get('id')
        comment = Comment.objects.get(id=id)
        if not self.request.user == comment.author:
            raise PermissionDenied
        else: 
            return comment


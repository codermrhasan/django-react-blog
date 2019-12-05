from django.views.generic.list import ListView
from blog.models import Post
from django.shortcuts import render
from django.db.models import Q

# def home_view(request):
#     return render(request, 'generic/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'generic/home.html'
    context_object_name = 'posts'
    paginate_by = 10

class SearchResultsView(ListView):
    template_name = 'generic/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
        query = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=query)|
            Q(body__icontains=query)
        )
        return posts
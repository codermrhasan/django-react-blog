from django.views.generic.list import ListView
from blog.models import Post
from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import TemplateView

# from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @cache_page(CACHE_TTL)
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

class AccountSettingsView(TemplateView):
    template_name = 'account/settings.html'
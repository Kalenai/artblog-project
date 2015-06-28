from django.views.generic import ListView, DetailView
from . import models


class BlogIndex(ListView):
    queryset = models.Post.objects.published()
    paginate_by = 2
    template_name = 'blog/blog-index.html'


class BlogDetail(DetailView):
    model = models.Post
    template_name = 'blog/blog-detail.html'

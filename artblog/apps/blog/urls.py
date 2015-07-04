from django.conf.urls import url
from .views import BlogIndex, BlogDetail

urlpatterns = [
    url(r'^$', BlogIndex.as_view(), name="blog_index"),
    url(r'^post/(?P<slug>\S+)$', BlogDetail.as_view(), name="post_detail"),
]

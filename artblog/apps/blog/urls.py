from django.conf.urls import url
from .views import BlogIndex

urlpatterns = [
    url(r'^$', BlogIndex, name="index")
]

from django.conf.urls import url
from .views import GalleryIndex, GalleryDetail

urlpatterns = [
    url(r'^$', GalleryIndex.as_view(), name="gallery_index"),
]

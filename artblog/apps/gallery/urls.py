from django.conf.urls import url
from .views import GalleryIndex

urlpatterns = [
    url(r'^$', GalleryIndex.as_view(), name="gallery_index"),
]

from django.views.generic import ListView
from . import models

class GalleryIndex(ListView):
    queryset = models.ImageEntry.objects.visible()
    paginate_by = 6
    template_name = 'gallery/gallery-index.html'


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from .views import home, home_files

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('artblog.apps.blog.urls')),
    url(r'^gallery/', include('artblog.apps.gallery.urls')),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Only for development!

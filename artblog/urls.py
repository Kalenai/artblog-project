from django.conf.urls import include, url
from django.contrib import admin
from .views import home, home_files

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^blog/', include('artblog.apps.blog.urls')),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'})
]

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'SF_Movies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include('movies.urls')),
    url(r'^$', RedirectView.as_view(url='/movies')),
    url(r'^movies/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

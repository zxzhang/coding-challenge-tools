from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

RedirectView.permanent = True

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/movies')),
    url(r'^movies/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

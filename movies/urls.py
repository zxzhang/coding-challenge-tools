'''
Created on Apr 28, 2015

@author: Polarbear
'''

from django.conf.urls import url

from movies import mapViews

urlpatterns = [
    url(r'^$', mapViews.index, name='index'),
    # url(r'^get-all-movies$', mapViews.getAllMovies),
    url(r'^get-title$', mapViews.getTitle, name='title'),
    url(r'^get-address$', mapViews.getAddress, name='address'),
    url(r'^get-company$', mapViews.getCompany, name='company'),
    url(r'^get-movies$', mapViews.search, name='search'),
]
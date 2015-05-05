'''
Created on Apr 28, 2015

@author: Polarbear
'''

from django.conf.urls import url

from movies import mapViews
# from movies import loginViews

urlpatterns = [
    url(r'^$', mapViews.index, name='index'),
    url(r'^get-all-movies$', mapViews.getAllMovies),
    url(r'^get-title$', mapViews.getTitle),
    url(r'^get-address$', mapViews.getAddress),
    url(r'^get-company$', mapViews.getCompany),
]
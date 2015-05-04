'''
Created on Apr 28, 2015

@author: Polarbear
'''

from django.conf.urls import url

from movies import mapViews
# from movies import loginViews

urlpatterns = [
    url(r'^$', mapViews.index, name='index'),
]
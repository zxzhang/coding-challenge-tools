from django.db import models
from datetime import datetime
# User class for built-in authentication module
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    gender = models.CharField(max_length=30, blank=True)
    picture = models.ImageField(upload_to="profile-photos", default='profile-photos/default.jpg', blank=True) 
    def __unicode__(self):
        return self.firstName+' '+self.lastName
    @staticmethod
    def get_userinfo(user):
        return UserInfo.objects.get(user=user)
    
class movies(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    fun_facts = models.CharField(max_length=500)
    production_company = models.CharField(max_length=100)
    distributor = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    actor1 = models.CharField(max_length=100)
    actor2 = models.CharField(max_length=100)
    actor3 = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title + ' ' + self.location
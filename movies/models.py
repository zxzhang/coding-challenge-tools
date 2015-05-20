from django.db import models
# from datetime import datetime
# User class for built-in authentication module

class Movie(models.Model):
    title = models.CharField(db_index=True, max_length=100)
    release_year = models.CharField(max_length=50)
    location = models.CharField(db_index=True, max_length=200)
    fun_facts = models.CharField(max_length=500)
    production_company = models.CharField(db_index=True, max_length=100)
    distributor = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    actor1 = models.CharField(max_length=100)
    actor2 = models.CharField(max_length=100)
    actor3 = models.CharField(max_length=100)
    latitude =  models.FloatField()
    longitude = models.FloatField()
    def __unicode__(self):
        return self.title + ': ' + self.location

class Title(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    def __unicode__(self):
        return self.title
    
class Address(models.Model):
    location = models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
        return self.location

class Company(models.Model):
    production_company = models.CharField(max_length=100, primary_key=True)
    def __unicode__(self):
        return self.production_company
    
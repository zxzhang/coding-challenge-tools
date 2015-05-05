from django.shortcuts import render
from django.http import HttpResponse
from models import Movies
from models import Title
from models import Address
from models import Company

def index(request):
    return render(request, 'movies/searchbox.html', {})
    # return HttpResponse("Hello, world. You're at the movies.")
    
def getAllMovies(request):
    context = {'movies' : Movies.objects.all()}
    return render(request, 'movies/movies.xml', context, content_type='application/xml');

def getTitle(request):
    context = {'titles' : Title.objects.all()}
    return render(request, 'movies/title.xml', context, content_type='application/xml');

def getAddress(request):
    context = {'addresses' : Address.objects.all()}
    return render(request, 'movies/address.xml', context, content_type='application/xml');

def getCompany(request):
    context = {'companies' : Company.objects.all()}
    return render(request, 'movies/company.xml', context, content_type='application/xml');
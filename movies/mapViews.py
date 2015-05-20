from django.shortcuts import render
from models import Movie
from models import Title
from models import Address
from models import Company
from django.http import JsonResponse

# main google map and search box page
def index(request):
    return render(request, 'movies/searchbox.html', {})
    
'''
def getAllMovies(request):
    context = {'movies' : Movie.objects.all()}
    return render(request, 'movies/movies.xml', context, content_type='application/xml');
'''

# get the movies through the title
def getTitle(request):
    titles = []
    if request.method == 'POST' and request.is_ajax():
        if 'term' in request.POST and request.POST['term']:
            items = Title.objects.filter(title__icontains=request.POST['term'])
            titles = [item.title for item in items]
    return JsonResponse(titles, safe=False)

# get the movies through the address
def getAddress(request):
    addresses = []
    if request.method == 'POST' and request.is_ajax():
        if 'term' in request.POST and request.POST['term']:
            items = Address.objects.filter(location__icontains=request.POST['term'])
            addresses = [item.location for item in items]
    return JsonResponse(addresses, safe=False)

# get the movies through the company
def getCompany(request):
    companies = []
    if request.method == 'POST' and request.is_ajax():
        if 'term' in request.POST and request.POST['term']:
            items = Company.objects.filter(production_company__icontains=request.POST['term'])
            companies = [item.production_company for item in items]
    return JsonResponse(companies, safe=False)

# get the search result data
def search(request):
    print request
    context = {}
    if request.method == "POST" and request.is_ajax():
        if 'content' in request.POST and request.POST['content'] \
            and 'term' in request.POST and request.POST['term']:
            if request.POST['content'] == 'title':
                context['movies'] = Movie.objects.filter(title__icontains=request.POST['term'])
            elif request.POST['content'] == 'location':
                context['movies'] = Movie.objects.filter(location__icontains=request.POST['term'])
            else:
                context['movies'] = Movie.objects.filter(production_company__icontains=request.POST['term'])
    return render(request, 'movies/movies.xml', context, content_type='application/xml');
        
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'movies/test_map.html', {})
    # return HttpResponse("Hello, world. You're at the movies.")
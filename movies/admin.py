from django.contrib import admin

from .models import Movie
from .models import Title
from .models import Address
from .models import Company

admin.site.register(Movie)
admin.site.register(Title)
admin.site.register(Address)
admin.site.register(Company)


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User, Film

# Create your views here.

def index(request):
    return HttpResponse('Inventory')

def list(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'inventory/list.html', {'films': user.films.all()})

def details(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return HttpResponse('This is film {}'.format(film_id))

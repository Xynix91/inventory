from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import User, Film, Series

# Create your views here.

def index(request):
    return HttpResponse('Inventory')

def login(request):
    return render(request, 'inventory/login.html')

def login_failed(request):
    return render(request, 'inventory/login_failed.html', {
        'prev_email': request.session['prev_email'],
        'prev_pass': request.session['prev_pass']
    })

def verify(request):
    email_entry = request.POST['email']
    pass_entry = request.POST['pass']

    user = User.objects.get(email=email_entry)
    if user.password == pass_entry:
        request.session['user_id'] = user.id
        return HttpResponseRedirect('/inventory/list/')
    else:
        request.session['prev_email'] = email_entry
        request.session['prev_pass'] = pass_entry
        return HttpResponseRedirect('/inventory/login-failed/')

def list(request):
    user = User.objects.get(pk=request.session['user_id'])
    return render(request, 'inventory/list.html', {'films': user.films.all()})

def create(request):
    return render(request, 'inventory/create.html', {'series_list': Series.objects.all()})

def create_action(request):
    curr_user = User.objects.get(pk=request.session['user_id'])
    data = request.POST

    if data['title'] == '':
        return HttpResponseRedirect('/inventory/create/')

    film = Film(addition_date=timezone.now(), user=curr_user, name=data['title'])
    if 'standalone' not in data.keys():
        if len(Series.objects.filter(name=data['series'])) == 0:
            film.series = Series(name=data['series'])
            film.series.save()
        else:
            film.series = Series.objects.get(name=data['series'])
        film.ordinal = data['ordinal']
    film.save()
    return HttpResponseRedirect('/inventory/list/')

def details(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'inventory/details.html', {
        'film': film,
        'standalone_box': 'checked' if film.standalone() else '',
        'series_list': Series.objects.all()
    })

def edit(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    data = request.POST

    if data['title'] == '':
        return HttpResponseRedirect('/inventory/create/')
    film.name = data['title']

    if 'standalone' not in data.keys():
        if len(Series.objects.filter(name=data['series'])) == 0:
            film.series = Series(name=data['series'])
            film.series.save()
        else:
            film.series = Series.objects.get(name=data['series'])
        film.ordinal = data['ordinal']
    film.save()
    return HttpResponseRedirect('/inventory/list/')

def delete(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    film.delete()
    return HttpResponseRedirect('/inventory/list/')

from django.shortcuts import render
from django.http import HttpResponse

from .models import SuperheroApp

# Create your views here.
def index(request):
    all_heroes = SuperheroApp.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes_app/index.html', context)

def detail(request, hero_id):
    single_hero = SuperheroApp.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes_app/detail.html', context)
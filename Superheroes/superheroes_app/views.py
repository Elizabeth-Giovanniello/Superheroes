from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def create(request):
    if request.method == "POST":
        #save the form contents as a new db object
        #return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = SuperheroApp(name = name, alter_ego = alter_ego, primary_ability = primary, secondary_ability = secondary, catch_phrase = catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes_app:index'))

    else:
        return render(request, 'superheroes_app/create.html')
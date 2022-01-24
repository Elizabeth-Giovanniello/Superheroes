from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import SuperheroApp
from .forms import *
from django.core.files.storage import FileSystemStorage

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
        try: image = request.FILES['image']
        except: image = '/images/default.jpg'
        new_hero = SuperheroApp(name = name, alter_ego = alter_ego, primary_ability = primary, secondary_ability = secondary, catch_phrase = catchphrase, photo = image)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes_app:index'))

    else:
        return render(request, 'superheroes_app/create.html')

def edit(request, id):
    single_hero = SuperheroApp.objects.get(pk=id)
    if request.method == "POST":
        single_hero.name = request.POST.get('name')
        single_hero.alter_ego = request.POST.get('alter_ego')
        single_hero.primary_ability = request.POST.get('primary')
        single_hero.secondary_ability = request.POST.get('secondary')
        single_hero.catch_phrase = request.POST.get('catchphrase')
        single_hero.photo = request.FILES['image']
        single_hero.save(update_fields=['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase', 'photo'])
        return HttpResponseRedirect(reverse('superheroes_app:detail', kwargs={'hero_id': single_hero.id}))
    else:
        context = {
            'single_hero': single_hero
        }
        return render(request, 'superheroes_app/edit.html', context)

        #TODO come back and fix the link to bring us back to the details page

def delete(request, id):
    single_hero = SuperheroApp.objects.get(pk=id)
    single_hero.delete()
    return HttpResponseRedirect(reverse('superheroes_app:index'))



  
  

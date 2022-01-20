from django.urls import path

from . import views


app_name = 'superheroes_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail')
]
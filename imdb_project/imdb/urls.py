from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('movie/<movie_id>/',views.movie,name='movie'),
    path('actor/<actor_id>/',views.actor,name='actor'),
    path('director/<director_id>/',views.director,name='director'),
    path('delete/<movie_id>/',views.delete,name='delete'),
    path('analytics/',views.analytics,name='analytics'),
    path('analytics1/',views.analytics1,name='analytics1'),
]
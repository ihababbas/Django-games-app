from django.urls import path
from .views import guessing_game

urlpatterns = [
    path('guessing/',guessing_game, name= 'guessing')
    
]
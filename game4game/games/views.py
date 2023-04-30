from django.shortcuts import render
from django.views import generic
from .models import Game


class SingleGame(generic.DetailView):
    model = Game


class ListGames(generic.ListView):
    model = Game

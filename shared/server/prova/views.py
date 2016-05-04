# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context,loader
from prova.models import Film


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def gestione_film_handler(request):
    template = loader.get_template('gestione_film_main_page.html')
    return HttpResponse(template.render())


def inserisci_film_handler(request):
    template = loader.get_template('inserisci_film.html')
    film = Film.create("Pulp Fiction","Quentin Taratino")
    return HttpResponse(template.render())
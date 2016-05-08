# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from moviefy.forms import SalvaFilmForm,SalvaGenereForm
from moviefy.models import Film,Genere


def index(request):
    return render(request,'index.html')


def gestione_film_handler(request):
    return render(request,'gestione_film.html')


def inserisci_film_handler(request):
    generi = Genere.objects.all()
    return render(request,'inserisci_film.html',{'generi': generi})


def salva_film_handler(request):
    if request.method == 'POST':
        form = SalvaFilmForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            genere = request.POST.get('generi')
            film = Film.create(form_fields['titolo'],form_fields['regista'], Genere.objects.get(nome=genere))
            return render(request,'film_salvato.html',{'form_fields': form_fields, 'genere': genere})
    else:
        form = SalvaFilmForm()
    generi = Genere.objects.all()
    return render(request,'inserisci_film_form_non_valida.html',{'form': form, 'generi': generi})


def gestione_generi_handler(request):
    return render(request,'gestione_generi.html')


def inserisci_genere_handler(request):
    return render(request,'inserisci_genere.html')


def salva_genere_handler(request):
    if request.method == 'POST':
        form = SalvaGenereForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            genere = Genere.create(form_fields['nome'])
            return render(request,'genere_salvato.html',{'form_fields': form_fields})
    else:
        form = SalvaGenereForm()
    return render(request,'inserisci_genere_form_non_valida.html',{'form': form})
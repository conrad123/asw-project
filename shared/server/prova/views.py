# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from prova.forms import SalvaFilmForm,SalvaGenereForm
from prova.models import Film,Genere


def index(request):
    return render(request,'index.html')


def gestione_film_handler(request):
    return render(request,'gestione_film_main_page.html')


def inserisci_film_handler(request):
    generi = Genere.objects.all()
    return render(request,'inserisci_film.html',{'generi': generi})


def salva_film_handler(request):
    if request.method == 'POST':
        form = SalvaFilmForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            genere = Genere.objects.get(nome=form_fields['genere'])
            film = Film.create(form_fields['titolo'],form_fields['regista'], genere)
            return render(request,'film_salvato.html',{'form_fields': form_fields})
    else:
        form = SalvaFilmForm()
    return render(request,'inserisci_film_form_non_valida.html',{'form': form})



def gestione_generi_handler(request):
    return render(request,'gestione_generi.html')


def inserisci_genere_handler(request):
    return render(request,'inserisci_genere.html')


def salva_genere_handler(request):
    if request.method == 'POST':
        form = SalvaGenereForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            genere = Genere.create(form_fields['titolo'])
            return render(request,'genere_salvato.html',{'form_fields': form_fields})
    else:
        form = SalvaGenereForm()
    return render(request,'inserisci_genere_form_non_valida.html',{'form': form})
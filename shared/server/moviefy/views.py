# -*- coding: utf-8 -*-
from django.shortcuts import render
from moviefy.forms import SalvaFilmForm,SalvaGenereForm
from moviefy.models import Film,Genere
from django.db import IntegrityError


def index(request):
    return render(request,'index.html')


def inserisci_film_handler(request):
    generi = Genere.objects.all()
    return render(request,'inserisci_film.html',{'generi': generi})


def salva_film_handler(request):
    if request.method == 'POST':
        form = SalvaFilmForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            genere = request.POST.get('generi')
            try:
                film = Film.create(form_fields['titolo'],form_fields['regista'],form_fields['anno'], Genere.objects.get(nome=genere))
            except IntegrityError as erorr:
                message = 'Il film era già presente nel database, quindi non è stato duplicato.'
                return render(request,'film_salvato.html',{'form_fields': form_fields, 'genere': genere, 'message': message})
            return render(request,'film_salvato.html',{'form_fields': form_fields, 'genere': genere})
    else:
        form = SalvaFilmForm()
    generi = Genere.objects.all()
    return render(request,'inserisci_film_form_non_valida.html',{'form': form, 'generi': generi})


def inserisci_genere_handler(request):
    return render(request,'inserisci_genere.html')


def salva_genere_handler(request):
    if request.method == 'POST':
        form = SalvaGenereForm(request.POST)
        if form.is_valid():
            form_fields = form.cleaned_data
            try:
                genere = Genere.create(form_fields['nome'])
            except IntegrityError as error:
                message = 'Il genere era già presente nel database, quindi non è stato duplicato.'
                return render(request,'genere_salvato.html',{'form_fields': form_fields, 'message': message})
            return render(request,'genere_salvato.html',{'form_fields': form_fields})
    else:
        form = SalvaGenereForm()
    return render(request,'inserisci_genere_form_non_valida.html',{'form': form})


def catalogo_film_handler(request):
    films = Film.objects.all()
    generi = Genere.objects.all()
    return render(request,'catalogo_film.html',{'generi': generi, 'films': films})


def filtra_catalogo_handler(request):
    if request.method == 'POST':
        genere = request.POST.get('generi')
        films = Film.objects.values('titolo','regista').filter(genere=Genere.objects.get(nome=genere))
    generi = Genere.objects.all()
    return render(request,'catalogo_filtrato.html',{'genere': genere, 'generi': generi, 'films': films})
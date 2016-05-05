# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from prova.forms import SalvaFilmForm
from prova.models import Film


def index(request):
    return render(request,'index.html')


def gestione_film_handler(request):
    return render(request,'gestione_film_main_page.html')


def inserisci_film_handler(request):
    return render(request,'inserisci_film.html')


def salva_film_handler(request):
	if request.method == 'POST':
		form = SalvaFilmForm(request.POST)
		if form.is_valid():
			form_fields = form.cleaned_data
			film = Film.create(form_fields['titolo'],form_fields['regista'])
			return render(request,'film_salvato.html',{'form_fields': form_fields})
	else:
		form = SalvaFilmForm()
	return render(request,'inserisci_film_form_non_valida.html',{'form': form})
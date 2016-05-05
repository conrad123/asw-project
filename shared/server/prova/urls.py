"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^gestione-film/', 'prova.views.gestione_film_handler'),
    url(r'^gestione-generi/', 'prova.views.gestione_generi_handler'),
    url(r'^inserisci-genere/', 'prova.views.inserisci_genere_handler'),
    url(r'^inserisci-film/', 'prova.views.inserisci_film_handler'),
    url(r'^salva-film/', 'prova.views.salva_film_handler'),
    url(r'^salva-genere/', 'prova.views.salva_genere_handler'),
    url(r'', 'prova.views.index'),
]
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gestione-film/', 'moviefy.views.gestione_film_handler'),
    url(r'^inserisci-film/', 'moviefy.views.inserisci_film_handler'),
    url(r'^salva-film/', 'moviefy.views.salva_film_handler'),
    url(r'^gestione-generi/', 'moviefy.views.gestione_generi_handler'),
    url(r'^inserisci-genere/', 'moviefy.views.inserisci_genere_handler'),
    url(r'^salva-genere/', 'moviefy.views.salva_genere_handler'),
    url(r'^catalogo-film/', 'moviefy.views.catalogo_film_handler'),
    url(r'filtra-catalogo/', 'moviefy.views.filtra_catalogo_handler'),
    url(r'', 'moviefy.views.index'),
]
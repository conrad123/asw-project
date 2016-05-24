from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from moviefy.serializers import GenereViewSet, FilmViewSet

router = routers.DefaultRouter()
router.register(r'generi', GenereViewSet)
router.register(r'film', FilmViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^inserisci-film/', 'moviefy.views.inserisci_film_handler'),
    url(r'^salva-film/', 'moviefy.views.salva_film_handler'),
    url(r'^inserisci-genere/', 'moviefy.views.inserisci_genere_handler'),
    url(r'^salva-genere/', 'moviefy.views.salva_genere_handler'),
    url(r'^catalogo-film/', 'moviefy.views.catalogo_film_handler'),
    url(r'^filtra-catalogo/', 'moviefy.views.filtra_catalogo_handler'),
    url(r'', 'moviefy.views.index'),
]
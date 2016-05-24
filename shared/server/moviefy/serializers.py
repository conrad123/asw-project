from moviefy.models import Genere, Film
from rest_framework import serializers, viewsets


class GenereSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genere
        fields = ['pk', 'nome']


class GenereViewSet(viewsets.ModelViewSet):
    queryset = Genere.objects.all()
    serializer_class = GenereSerializer


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['pk', 'titolo','regista','anno','genere']


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
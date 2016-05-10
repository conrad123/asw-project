from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genere(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    @classmethod
    def create(cls,nome):
        genere = cls(nome=nome)
        genere.save()
        return genere


class Film(models.Model):
    titolo = models.CharField(max_length=30)
    regista = models.CharField(max_length=30)
    anno = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1890)])
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)

    @classmethod
    def create(cls,titolo,regista,anno,genere):
        film = cls(titolo=titolo,regista=regista,anno=anno,genere=genere)
        film.save()
        return film
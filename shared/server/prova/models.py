
from django.db import models


class Film(models.Model):
    titolo = models.CharField(max_length=30)
    regista = models.CharField(max_length=30)

    @classmethod
    def create(cls,titolo,regista):
        film = cls(titolo=titolo,regista=regista)
        film.save()
        return film
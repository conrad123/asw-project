from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class SalvaFilmForm(forms.Form):
    titolo = forms.CharField(label='titolo', max_length=30)
    regista = forms.CharField(label='regista', max_length=30)
    anno = forms.IntegerField(label='anno', validators=[MaxValueValidator(99999),MinValueValidator(1890)])


class SalvaGenereForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=30)
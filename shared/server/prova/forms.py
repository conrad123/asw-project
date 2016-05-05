from django import forms


class SalvaFilmForm(forms.Form):
    titolo = forms.CharField(label='titolo', max_length=30)
    regista = forms.CharField(label='regista', max_length=30)
    genere = forms.CharField(label='genere', max_length=30)


class SalvaGenereForm(forms.Form):
	titolo = forms.CharField(label='titolo', max_length=30)
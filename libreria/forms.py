from django import forms
from .models import Modelo_libros, Genero

class LibroForm(forms.ModelForm):
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())
    class Meta:
        model=Modelo_libros
        fields='__all__'
        

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields ='__all__'

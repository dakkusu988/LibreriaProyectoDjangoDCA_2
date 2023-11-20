from django import forms
from .models import Libreria

class LibreriaForm(forms.ModelForm):
    class Meta:
        model = Libreria
        fields = ['title', 'author', 'rating']

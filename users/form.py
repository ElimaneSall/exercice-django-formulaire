from django import  forms

from .models import Professeur


class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = "__all__"
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #dd9933'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #dd9933'}),
            'email': forms.EmailInput(attrs={'placeholder':'example@ept.sn','class': 'form-control', 'style':'border:2px solid #dd9933'}),
            'contact': forms.TextInput(attrs={'placeholder':'+221 xx xxx xx xx','class': 'form-control', 'style':'border:2px solid #dd9933'}),
            'Date_adhesion': forms.DateInput(attrs={'placeholder':'yyyy-mm-dd','class': 'form-control', 'style':'border:2px solid #dd9933'}),
        }


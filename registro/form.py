from django import forms
from proyecto.models import USUARIO, DUENO
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms.formsets import all_valid


class registro(forms.ModelForm):
    class Meta:
        widgets = {
        'password': forms.PasswordInput(),
        
        }

        fields = ('first_name', 'last_name', 'email', 'genero', 'password', 'tipoDocumento', 'numero_Documento', 'fecha_nacimiento',
                  'direccion', 'telefono' )
        model = USUARIO



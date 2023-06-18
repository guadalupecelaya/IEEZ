from django import forms
from .models import Departamentos

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'
        widgets = {
            # 'nombre':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre del Material', 'onFOcus':'validar{this}'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }
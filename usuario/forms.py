from django import forms
from .models import Usuario



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'forms-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UsuarioFormLog(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('__all__')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'forms-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super(UsuarioFormLog, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

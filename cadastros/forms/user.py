from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from cadastros.models import Perfil

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email_formulario = self.cleaned_data['email']
        if(User.objects.filter(email=email_formulario).exists()):
            raise ValidationError("O email {} já está em uso".format(email_formulario))
        return email_formulario

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'cpf', 'telefone', 'whatsapp', 'cidade']

    def clean(self):
        self.cleaned_data['telefone'] = self.cleaned_data['telefone'].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        self.cleaned_data['whatsapp'] = self.cleaned_data['whatsapp'].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        self.cleaned_data['cpf'] = self.cleaned_data['cpf'].replace('-', '').replace('.', '')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs['class'] = 'phone'
        self.fields['whatsapp'].widget.attrs['class'] = 'phone'
        self.fields['cpf'].widget.attrs['class'] = 'cpf'
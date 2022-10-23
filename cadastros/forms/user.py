from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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

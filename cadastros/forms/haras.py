from django import forms
from ..models import Haras

class HarasForm(forms.ModelForm):
    class Meta:
        model = Haras
        fields = ['nome', 'descricao', 'telefone_primario',
                  'telefone_secundario', 'cidade', 'logo']

    def clean(self):
        self.cleaned_data['telefone_primario'] = self.cleaned_data['telefone_primario'].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        self.cleaned_data['telefone_secundario'] = self.cleaned_data['telefone_secundario'].replace(
            ' ', '').replace('(', '').replace(')', '').replace('-', '')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone_primario'].widget.attrs['class'] = 'phone'
        self.fields['telefone_secundario'].widget.attrs['class'] = 'phone'

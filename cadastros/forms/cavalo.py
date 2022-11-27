from django import forms
from ..models import Cavalo

class CavaloForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    class Meta:
        model = Cavalo
        fields = ["nome", "preco", "data_nascimento", "descricao", "registro", "raca", "pelagem", "genero", "habilidade", "cidade", "haras"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['haras'].queryset = self.fields['haras'].queryset.filter(
            proprietario=user)
        self.fields['preco'].widget.attrs['class'] = 'money'

class ImagemForm(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False
    )
    class Meta: 
        fields = ["imagem"]

class CavaloImagemForm(CavaloForm, ImagemForm):

    class Meta(CavaloForm.Meta, ImagemForm.Meta):
        fields = CavaloForm.Meta.fields + ImagemForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


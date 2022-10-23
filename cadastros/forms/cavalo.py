from django import forms
from ..models import Cavalo

class CavaloForm(forms.ModelForm):
    class Meta:
        model = Cavalo
        fields = ["nome", "preco", "data_nascimento", "descricao", "registro", "raca", "pelagem", "genero", "habilidade", "cidade"]

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


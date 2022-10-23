from django.views.generic.edit import CreateView
from cadastros.forms.user import UsuarioForm
from django.urls import reverse_lazy

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registrar-se"
        context['botao'] = "Cadastrar-se"

        return context
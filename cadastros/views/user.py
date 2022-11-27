from django.views.generic.edit import CreateView, UpdateView
from cadastros.forms.user import UsuarioForm
from django.urls import reverse_lazy
from django.contrib import messages

from cadastros.models import Perfil

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        url = super().form_valid(form)

        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registrar-se"
        context['botao'] = "Cadastrar-se"

        return context

class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone", "whatsapp", "cidade"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        perfil = ""
        try:
            perfil = Perfil.objects.get(usuario=self.request.user)
        except Perfil.DoesNotExist:
            perfil = Perfil.objects.create(usuario=self.request.user)
            perfil.save()
            
        self.object = perfil

        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus dados"
        context['botao'] = "Alterar"

        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Informações do perfil atualizadas com sucesso")
        return url

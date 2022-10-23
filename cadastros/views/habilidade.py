from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from cadastros.models import Habilidade

class HabilidadesList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Administrador"]
    model = Habilidade
    template_name = 'listas/habilidades.html'


class HabilidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador"]
    model = Habilidade
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-habilidades')

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Habilidade cadastrada com sucesso")
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Habilidade"

        return context


class HabilidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador"]
    model = Habilidade
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-habilidades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Habilidade"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Habilidade, pk=self.kwargs['pk'])
        return self.object

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Habilidade alterada com sucesso")
        return url

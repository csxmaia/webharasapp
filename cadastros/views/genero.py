from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from cadastros.models import Genero


class GenerosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Administrador"]
    model = Genero
    template_name = 'listas/generos.html'


class GeneroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador"]
    model = Genero
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos')

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Gênero cadastrada com sucesso")
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Gênero"

        return context


class GeneroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador"]
    model = Genero
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-generos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Gênero"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Genero, pk=self.kwargs['pk'])
        return self.object

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Gênero alterada com sucesso")
        return url

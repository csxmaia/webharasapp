from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db import models

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


class DeletarGenero(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            genero = get_object_or_404(Genero, pk=pk)
            if genero:
                nome_genero = genero.tipo
                try:
                    genero.delete()
                    messages.success(self.request, "{nome_genero} deletado com sucesso!".format(
                        nome_genero=nome_genero))
                except models.ProtectedError:
                    messages.warning(self.request, "{nome_genero} é impossivel de ser deletado pois é utilizado em Cavalos já registrados!".format(
                        nome_genero=nome_genero))

                return redirect("listar-generos")

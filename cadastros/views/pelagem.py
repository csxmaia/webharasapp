from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db import models

from cadastros.models import Pelagem


class PelagensList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Administrador"]
    model = Pelagem
    template_name = 'listas/pelagens.html'


class PelagemCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador"]
    model = Pelagem
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pelagens')

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Pelagem cadastrada com sucesso")
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Pelagem"

        return context


class PelagemUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador"]
    model = Pelagem
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pelagens')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Pelagem"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pelagem, pk=self.kwargs['pk'])
        return self.object

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Pelagem alterada com sucesso")
        return url


class DeletarPelagem(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            pelagem = get_object_or_404(Pelagem, pk=pk)
            if pelagem:
                nome_pelagem = pelagem.nome
                try:
                    pelagem.delete()
                    messages.success(self.request, "{nome_pelagem} deletado com sucesso!".format(
                        nome_pelagem=nome_pelagem))
                except models.ProtectedError:
                    messages.warning(self.request, "{nome_pelagem} é impossivel de ser deletado pois é utilizado em Cavalos já registrados!".format(
                        nome_pelagem=nome_pelagem))

                return redirect("listar-pelagens")

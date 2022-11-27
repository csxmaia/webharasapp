from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db import models

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


class DeletarHabilidade(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            habilidade = get_object_or_404(Habilidade, pk=pk)
            if habilidade:
                nome_habilidade = habilidade.tipo
                try:
                    habilidade.delete()
                    messages.success(self.request, "{nome_habilidade} deletado com sucesso!".format(
                        nome_habilidade=nome_habilidade))
                except models.ProtectedError:
                    messages.warning(self.request, "{nome_habilidade} é impossivel de ser deletado pois é utilizado em Cavalos já registrados!".format(
                        nome_habilidade=nome_habilidade))

                return redirect("listar-habilidades")

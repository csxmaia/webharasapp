from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db import models

from cadastros.models import Raca

class RacasList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Administrador"]
    model = Raca
    template_name = 'listas/racas.html'

class RacaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador"]
    model = Raca
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-racas')

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Raça cadastrada com sucesso")
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Raça"

        return context


class RacaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador"]
    model = Raca
    fields = '__all__'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-racas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Raça"

        return context
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Raca, pk=self.kwargs['pk'])
        return self.object

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Raça alterada com sucesso")
        return url


class DeletarRaca(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            raca = get_object_or_404(Raca, pk=pk)
            if raca:
                nome_raca = raca.nome
                try:
                    raca.delete()
                    messages.success(self.request, "{nome_raca} deletado com sucesso!".format(
                    nome_raca=nome_raca))
                except models.ProtectedError:
                    messages.warning(self.request, "{nome_raca} é impossivel de ser deletado pois é utilizado em Cavalos já registrados!".format(
                        nome_raca=nome_raca))

                return redirect("listar-racas")

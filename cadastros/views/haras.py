
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cadastros.forms.haras import HarasForm

from cadastros.models import Haras


class HarasCreate(LoginRequiredMixin, CreateView):
    form_class = HarasForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('dashboard-haras')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Haras"

        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.modificado_por = self.request.user
        form.instance.proprietario = self.request.user
        form.instance.status = "EM ANÁLISE"

        url = super().form_valid(form)

        messages.success(self.request, "Haras salvo com sucesso.")
        messages.success(self.request, "Seu Haras está em análise.")
        return url


class HarasUpdate(LoginRequiredMixin, UpdateView):
    form_class = HarasForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('dashboard-haras')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Haras"

        return context

    def get_object(self, queryset=None):
        haras = get_object_or_404(Haras, pk=self.kwargs['pk'])
        self.object = haras

        return self.object

    def form_valid(self, form):
        form.instance.modificado_por = self.request.user
        form.instance.status = "EM ANÁLISE"
        url = super().form_valid(form)

        messages.success(self.request, "Haras alterado com sucesso.")
        messages.success(self.request, "Seu haras está em análise.")
        return url

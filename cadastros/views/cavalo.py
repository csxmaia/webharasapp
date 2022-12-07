from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from cadastros.forms.cavalo import CavaloImagemForm

from cadastros.models import Cavalo, Imagem

class CavaloCreate(LoginRequiredMixin, CreateView):
    form_class = CavaloImagemForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('dashboard-cavalos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Cavalo"

        return context

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.modificado_por = self.request.user
        form.instance.proprietario = self.request.user
        form.instance.status = "EM ANÁLISE"
        
        url = super().form_valid(form)
        
        files = self.request.FILES.getlist("imagem")
        for imagem in files:
            Imagem.objects.create(cavalo=form.instance, imagem=imagem)

        messages.success(self.request, "Cavalo salvo com sucesso.")
        messages.success(self.request, "Seu cavalo está em análise.")
        return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CavaloUpdate(LoginRequiredMixin, UpdateView):
    form_class = CavaloImagemForm
    template_name = 'cadastros/cavalo_form.html'
    success_url = reverse_lazy('dashboard-cavalos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cavalo"

        # imagens = get_list_or_404(Imagem, cavalo=self.kwargs['pk'])
        # context['imagens'] = imagens
        # self.request.FILES.setlist("imagem", imagens)

        return context
        
    def get_object(self, queryset=None):
        cavalo = get_object_or_404(Cavalo, pk=self.kwargs['pk'])
        self.object = cavalo

        imagens = get_list_or_404(Imagem, cavalo=cavalo)
        #TODO: Implementar imagens atuais para atualizar imagem 

        # self.object.imagem = imagens
        # self.request.FILES.setlist("imagem", imagens)

        return self.object

    def form_valid(self, form):
        form.instance.modificado_por = self.request.user
        form.instance.status = "EM ANÁLISE"
        url = super().form_valid(form)

        #TODO check new images after update
        files = self.request.FILES.getlist("imagem")
        print(files)
        for imagem in files:
            Imagem.objects.create(cavalo=form.instance, imagem=imagem)

        messages.success(self.request, "Cavalo alterado com sucesso.")
        messages.success(self.request, "Seu cavalo está em análise.")
        return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

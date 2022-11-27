from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView, View
from cadastros.models import Cavalo, Haras, Imagem
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

class DashboardUserHaras(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user/haras.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        todos_cavalos_usuario_EM_ANALISE_query = Haras.objects.order_by(
            '-id').filter(status="EM ANÁLISE", criado_por=self.request.user)
        context['todos_cavalos_usuario_EM_ANALISE'] = todos_cavalos_usuario_EM_ANALISE_query

        todos_cavalos_usuario_NAO_EM_ANALISE_query = Haras.objects.order_by(
            '-id').exclude(status="EM ANÁLISE").filter(criado_por=self.request.user)
        context['todos_cavalos_usuario_NAO_EM_ANALISE'] = todos_cavalos_usuario_NAO_EM_ANALISE_query

        return context


class DashboardAdminHaras(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = [u"Administrador"]
    template_name = 'dashboard/admin/haras.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        todos_cavalos_EM_ANALISE_query = Haras.objects.filter(status="EM ANÁLISE").order_by('-id')
        context['todos_cavalos_em_analise'] = todos_cavalos_EM_ANALISE_query

        todos_cavalos_APROVADOS_query = Haras.objects.exclude(status="EM ANÁLISE").order_by('-id')
        context['todos_cavalos_aprovados'] = todos_cavalos_APROVADOS_query

        return context

class VisualizarHaras(TemplateView):
    template_name = 'haras/visualizar_haras.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        haras = get_object_or_404(Haras, pk=self.kwargs['pk'])
        context['haras'] = haras

        try:
            todos_cavalos_haras = []
            todos_cavalos_haras_query = Cavalo.objects.filter(
                status="APROVADO", haras=haras).order_by('-id')

            for cavalo in todos_cavalos_haras_query:
                cavalo_obj = {'obj': {'cavalo': cavalo,
                                    "imagens": Imagem.objects.filter(cavalo=cavalo)}}
                todos_cavalos_haras.append(cavalo_obj)
            context['cavalos'] = todos_cavalos_haras
        except Cavalo.DoesNotExist:
            context['cavalos'] = []

        return context


class AlterarStatusHaras(View):
    def get(self, request, pk, status):
        user = request.user
        if user.is_authenticated:
            haras = get_object_or_404(Haras, pk=pk)

            if haras:
                haras.status = status
                haras.save()

                return redirect("admin-dashboard-haras")

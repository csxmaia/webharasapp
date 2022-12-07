from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView, View
from cadastros.models import Cavalo, Imagem
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

class DashboardUserCavalos(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user/cavalo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        todos_cavalos_usuario_EM_ANALISE_query = Cavalo.objects.order_by(
            '-id').filter(status="EM ANÁLISE", criado_por=self.request.user)
        todos_cavalos_usuario_EM_ANALISE = []
        # TODO criar query in()
        for cavalo in todos_cavalos_usuario_EM_ANALISE_query:
            cavalo_obj = {'obj': {'cavalo': cavalo, "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            todos_cavalos_usuario_EM_ANALISE.append(cavalo_obj)
        context['todos_cavalos_usuario_EM_ANALISE'] = todos_cavalos_usuario_EM_ANALISE

        todos_cavalos_usuario_NAO_EM_ANALISE_query = Cavalo.objects.order_by(
            '-id').exclude(status="EM ANÁLISE").filter(criado_por=self.request.user)
        todos_cavalos_usuario_NAO_EM_ANALISE = []
        # TODO criar query in()
        for cavalo in todos_cavalos_usuario_NAO_EM_ANALISE_query:
            cavalo_obj = {'obj': {'cavalo': cavalo, "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            todos_cavalos_usuario_NAO_EM_ANALISE.append(cavalo_obj)
        context['todos_cavalos_usuario_NAO_EM_ANALISE'] = todos_cavalos_usuario_NAO_EM_ANALISE

        return context


class DashboardAdminCavalos(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = [u"Administrador"]
    template_name = 'dashboard/admin/cavalo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        todos_cavalos_EM_ANALISE = []
        todos_cavalos_EM_ANALISE_query = Cavalo.objects.filter(status="EM ANÁLISE").order_by('-id')
        # TODO criar query in()
        for cavalo in todos_cavalos_EM_ANALISE_query:
            cavalo_obj = {'obj': {'cavalo': cavalo,
                                  "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            todos_cavalos_EM_ANALISE.append(cavalo_obj)
        context['todos_cavalos_em_analise'] = todos_cavalos_EM_ANALISE

        todos_cavalos_APROVADOS_REPROVADOS = []
        todos_cavalos_APROVADOS_REPROVADOS_query = Cavalo.objects.filter(status__in=("APROVADO", "REPROVADO")).order_by('-id')
        for cavalo in todos_cavalos_APROVADOS_REPROVADOS_query:
            cavalo_obj = {'obj': {'cavalo': cavalo,
                                  "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            todos_cavalos_APROVADOS_REPROVADOS.append(cavalo_obj)
        context['todos_cavalos_aprovados_reprovados'] = todos_cavalos_APROVADOS_REPROVADOS

        todos_cavalos_VENDIDOS = []
        todos_cavalos_VENDIDOS_query = Cavalo.objects.filter(status="VENDIDO").order_by('-id')
        for cavalo in todos_cavalos_VENDIDOS_query:
            cavalo_obj = {'obj': {'cavalo': cavalo,
                                  "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            todos_cavalos_VENDIDOS.append(cavalo_obj)
        context['todos_cavalos_vendidos'] = todos_cavalos_VENDIDOS

        return context

class VisualizarCavalo(TemplateView):
    template_name = 'cavalo/visualizar_cavalo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        cavalo = get_object_or_404(Cavalo, pk=self.kwargs['pk'])
        context['cavalo'] = cavalo

        imagens = Imagem.objects.filter(cavalo=self.kwargs['pk'])
        context['imagens'] = imagens

        return context

class AlterarStatusCavalo(View):
    def get(self, request, pk, status):
        user = request.user
        if user.is_authenticated:
            cavalo = get_object_or_404(Cavalo, pk=pk)

            if cavalo:
                cavalo.status = status
                cavalo.save()

                messages.success(self.request, "{nome_cavalo} ({id_cavalo}) alterado para {status}".format(nome_cavalo=cavalo.nome, id_cavalo=cavalo.pk, status=cavalo.status.capitalize()))
                
                if(user.groups.filter(name="Administrador").exists()):
                    return redirect("admin-dashboard-cavalos")
                else:
                     return redirect("dashboard-cavalos")


class DeletarCavalo(View):
    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            cavalo = get_object_or_404(Cavalo, pk=pk)
            if cavalo:
                nome_cavalo = cavalo.nome
                cavalo.delete()

                messages.success(self.request, "{nome_cavalo} deletado com sucesso!".format(
                    nome_cavalo=nome_cavalo))
                    
                if(user.groups.filter(name="Administrador").exists()):
                    return redirect("admin-dashboard-cavalos")
                else:
                     return redirect("dashboard-cavalos")

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView

from cadastros.models import Cavalo, Cidade, Genero, Habilidade, Imagem, Pelagem, Raca


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        raca = Raca.objects.all()
        context['racas'] = raca
        pelagem = Pelagem.objects.all()
        context['pelagens'] = pelagem
        generos = Genero.objects.all()
        context['generos'] = generos
        habilidade = Habilidade.objects.all()
        context['habilidades'] = habilidade
        cidade = Cidade.objects.all()
        context['cidades'] = cidade

        filters = Q(status="APROVADO")
        print( self.request.GET.get('raca'))
        if self.request.GET.get('raca') is not None:
            raca = self.request.GET.get('raca').replace("_", " ")
            filters &= Q(raca__nome__iexact=raca)
        if self.request.GET.get('pelagem') is not None:
            pelagem = self.request.GET.get('pelagem').replace("_", " ")
            filters &= Q(pelagem__nome__iexact=pelagem)
        if self.request.GET.get('genero') is not None:
            genero = self.request.GET.get('genero').replace("_", " ")
            filters &= Q(genero__tipo__iexact=genero)
        if self.request.GET.get('habilidade') is not None:
            habilidade = self.request.GET.get('habilidade').replace("_", " ")
            filters &= Q(habilidade__tipo__iexact=habilidade)
        if self.request.GET.get('cidade') is not None:
            cidade = self.request.GET.get('cidade').replace("_", " ")
            filters &= Q(cidade__nome__iexact=cidade)

        cavalos_query = Cavalo.objects.filter(filters).order_by('-id')

        paginator = Paginator(cavalos_query, 15)

        page_number = self.request.GET.get('page', 1)

        try:
            cavalos_query_page = paginator.page(page_number)
        except PageNotAnInteger:
            cavalos_query_page = paginator.page(1)
        except EmptyPage:
            cavalos_query_page = paginator.page(paginator.num_pages)

        context['cavalos_page'] = cavalos_query_page

        cavalos = []

        # TODO criar query in()
        for cavalo in cavalos_query_page:
            imagems = Imagem.objects.filter(cavalo=cavalo)
            cavalo_obj = {'obj': {'cavalo': cavalo, "imagens": imagems}}
            cavalos.append(cavalo_obj)

        context['cavalos'] = cavalos
        return context

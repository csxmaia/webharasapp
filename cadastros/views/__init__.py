from django.views.generic import TemplateView

from cadastros.models import Cavalo, Imagem

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        cavalos_query = Cavalo.objects.order_by('id')
        # cavalos = Cavalo.objects.order_by('-id')

        cavalos = []

        # TODO criar query in() 
        for cavalo in cavalos_query:
            imagems = Imagem.objects.filter(cavalo=cavalo)
            cavalo_obj = {'obj': {'cavalo': cavalo, "imagens": Imagem.objects.filter(cavalo=cavalo)}}
            cavalos.append(cavalo_obj)

        context['cavalos'] = cavalos
        return context
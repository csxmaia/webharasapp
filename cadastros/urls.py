from django.urls import path
from cadastros.views.cavalo import CavaloCreate, CavaloUpdate
from cadastros.views.genero import GeneroCreate, GeneroUpdate, GenerosList
from cadastros.views.habilidade import HabilidadeCreate, HabilidadeUpdate, HabilidadesList
from cadastros.views.pelagem import PelagemCreate, PelagemUpdate, PelagensList

from cadastros.views.raca import RacaCreate, RacaUpdate, RacasList
from cadastros.views.user import UsuarioCreate

ADMIN_DASHBOARD_PATH = "dashboard/admin/"

urlpatterns = [
    path('registrar/', UsuarioCreate.as_view(), name="auto-registro"),

    path(ADMIN_DASHBOARD_PATH + 'listar/racas', RacasList.as_view(), name="listar-racas"),
    path(ADMIN_DASHBOARD_PATH + 'cadastrar/raca', RacaCreate.as_view(), name="cadastrar-raca"),
    path(ADMIN_DASHBOARD_PATH + 'editar/raca/<int:pk>/', RacaUpdate.as_view(), name="editar-raca"),

    path(ADMIN_DASHBOARD_PATH + 'listar/pelagens', PelagensList.as_view(), name="listar-pelagens"),
    path(ADMIN_DASHBOARD_PATH + 'cadastrar/pelagem', PelagemCreate.as_view(), name="cadastrar-pelagem"),
    path(ADMIN_DASHBOARD_PATH + 'editar/pelagem/<int:pk>/', PelagemUpdate.as_view(), name="editar-pelagem"),

    path(ADMIN_DASHBOARD_PATH + 'listar/habilidades', HabilidadesList.as_view(), name="listar-habilidades"),
    path(ADMIN_DASHBOARD_PATH + 'cadastrar/habilidade', HabilidadeCreate.as_view(), name="cadastrar-habilidade"),
    path(ADMIN_DASHBOARD_PATH + 'editar/habilidade/<int:pk>/', HabilidadeUpdate.as_view(), name="editar-habilidade"),

    path(ADMIN_DASHBOARD_PATH + 'listar/generos', GenerosList.as_view(), name="listar-generos"),
    path(ADMIN_DASHBOARD_PATH + 'cadastrar/genero', GeneroCreate.as_view(), name="cadastrar-genero"),
    path(ADMIN_DASHBOARD_PATH + 'editar/genero/<int:pk>/', GeneroUpdate.as_view(), name="editar-genero"),

    path('cadastrar/cavalo', CavaloCreate.as_view(), name="cadastrar-cavalo"),
    path('editar/cavalo/<int:pk>/', CavaloUpdate.as_view(), name="editar-cavalo"),
    # path('cadastrar/cavalo/imagem/<int:cavalo_pk>/', ImagemCavaloCreate.as_view(), name="cadastrar-imagem-cavalo"),
]

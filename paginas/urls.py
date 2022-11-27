from django.urls import path

from paginas.views.cavalo import AlterarStatusCavalo, DashboardAdminCavalos, DashboardUserCavalos, DeletarCavalo, VisualizarCavalo
from paginas.views.haras import AlterarStatusHaras, DashboardAdminHaras, DashboardUserHaras, DeletarHaras, VisualizarHaras


from .views import IndexView

DASHBOARD_PATH = "dashboard/"
ADMIN_DASHBOARD_PATH = "dashboard/admin/"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path(DASHBOARD_PATH + 'cavalos', DashboardUserCavalos.as_view(), name="dashboard-cavalos"),
    path(DASHBOARD_PATH + 'haras', DashboardUserHaras.as_view(), name="dashboard-haras"),

    path(ADMIN_DASHBOARD_PATH + 'cavalos', DashboardAdminCavalos.as_view(), name="admin-dashboard-cavalos"),
    path(ADMIN_DASHBOARD_PATH + 'haras', DashboardAdminHaras.as_view(), name="admin-dashboard-haras"),
    # path(ADMIN_DASHBOARD_PATH + 'aprovar/<int:pk>/', AprovarCavalo.as_view(), name="admin-dashboard-aprovar-cavalo"),

    path('cavalo/<int:pk>/', VisualizarCavalo.as_view(), name="visualizar-cavalo"),
    path('haras/<int:pk>/<str:nome>', VisualizarHaras.as_view(), name="visualizar-haras"),

    path('alterar-status-cavalo/<int:pk>/<str:status>', AlterarStatusCavalo.as_view(), name="alterar-status-cavalo"),
    path('alterar-status-haras/<int:pk>/<str:status>', AlterarStatusHaras.as_view(), name="alterar-status-haras"),

    path('deletar-haras/<int:pk>', DeletarHaras.as_view(), name="deletar-haras"),
    path('deletar-cavalo/<int:pk>', DeletarCavalo.as_view(), name="deletar-cavalo"),
]

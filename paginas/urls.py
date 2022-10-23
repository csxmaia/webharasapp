from django.urls import path
from django.contrib.auth import views as auth_views

from paginas.views.cavalo import DashboardAdminCavalos, DashboardUserCavalos, VisualizarCavalo
from .views import IndexView

DASHBOARD_PATH = "dashboard/"
ADMIN_DASHBOARD_PATH = "dashboard/admin/"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html', extra_context={'titulo': 'Autenticação'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path(DASHBOARD_PATH + 'cavalos', DashboardUserCavalos.as_view(), name="dashboard-cavalos"),

    path(ADMIN_DASHBOARD_PATH + 'cavalos', DashboardAdminCavalos.as_view(), name="admin-dashboard-cavalos"),

    path('cavalo/<int:pk>/', VisualizarCavalo.as_view(), name="visualizar-cavalo"),

    # path('cavalo/<int:pk>/', VisualizarCavalo.as_view(), name="aprovar-cavalo"),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ServicioViewSet, HorarioViewSet, ReservaViewSet
from .api_views import reservas_hoy

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reservas-hoy/', reservas_hoy),
]
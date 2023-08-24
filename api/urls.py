from django.urls import path, include
from rest_framework import routers
from api.views import ParroquiaView, SectorView, BarrioView, DireccionView, UsuarioView

# Routers
router = routers.DefaultRouter()
router.register(r'parroquias', ParroquiaView, 'parroquia')
router.register(r'sector', SectorView, 'sector')
router.register(r'barrio', BarrioView, 'barrio')
router.register(r'direccion', DireccionView, 'direccion')
router.register(r'usuario', UsuarioView, 'usuario')

urlpatterns = [
    path('form/', include(router.urls))
]

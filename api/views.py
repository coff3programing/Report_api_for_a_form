from rest_framework import viewsets
from .models import Parroquia, Sector, Barrio, Direccion, Usuario
from .serializer import ParroquiaSerializer, SectorSerializer, BarrioSerializer, DireccionSerializer, UsuarioSerializer

class ParroquiaView(viewsets.ModelViewSet):
    serializer_class = ParroquiaSerializer
    queryset = Parroquia.objects.all()


class SectorView(viewsets.ModelViewSet):
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    

class BarrioView(viewsets.ModelViewSet):
    serializer_class = BarrioSerializer
    queryset = Barrio.objects.all()

    
class DireccionView(viewsets.ModelViewSet):
    serializer_class = DireccionSerializer
    queryset = Direccion.objects.all()

    
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
  
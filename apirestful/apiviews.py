from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *




class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#Tablas de la APP
class PaisViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer



class ProvinciaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [permissions.DjangoModelPermissions]



class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class MonedaViewSet(viewsets.ModelViewSet):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer
    permission_classes = [permissions.DjangoModelPermissions]




class TipodocumentoViewSet(viewsets.ModelViewSet):
    queryset            = Tipodocumento.objects.all()
    serializer_class    = TipodocumentoSerializer
    permission_classes  = [permissions.DjangoModelPermissions]



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset            = Empresa.objects.all()
    serializer_class    = EmpresaSerializer
    permission_classes  = [permissions.DjangoModelPermissions]


class OficinaViewSet(viewsets.ModelViewSet):
    queryset            = Oficina.objects.all()
    serializer_class    = OficinaSerializer
    permission_classes  = [permissions.DjangoModelPermissions]




class TipoAusenciaViewSet(viewsets.ModelViewSet):
    queryset            = TipoAusencia.objects.all()
    serializer_class    = TipoAusenciaSerializer
    permission_classes  = [permissions.IsAuthenticated]



class AusenciaViewSet(viewsets.ModelViewSet):
    queryset            = Ausencia.objects.all()
    serializer_class    = AusenciaSerializer
    permission_classes  = [permissions.DjangoModelPermissions]


class EquipoViewSet(viewsets.ModelViewSet):
    queryset            = Equipo.objects.all()
    serializer_class    = EquipoSerializer
    permission_classes  = [permissions.DjangoModelPermissions]



class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset            = Empleado.objects.all()
    serializer_class    = EmpleadoSerializer
    permission_classes  = [permissions.DjangoModelPermissions]


class TareaViewSet(viewsets.ModelViewSet):
    queryset            = Tarea.objects.all()
    serializer_class    = TareaSerializer
    permission_classes  = [permissions.DjangoModelPermissions]




class DiafestivoViewSet(viewsets.ModelViewSet):
    queryset            = Diafestivo.objects.all()
    serializer_class    = DiafestivoSerializer
    permission_classes  = [permissions.DjangoModelPermissions]

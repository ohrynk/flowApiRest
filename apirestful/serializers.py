from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Ciudad
        fields = '__all__'


class IdiomaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Idioma
        fields = '__all__'


class MonedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Moneda
        fields = ['nombre', 'sigla']


class TipodocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Tipodocumento
        fields = '__all__'


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Empresa
        fields = '__all__'


class OficinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Oficina
        fields = '__all__'


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Empleado
        fields = '__all__'

class TipoAusenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = TipoAusencia
        fields = '__all__'

class AusenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Ausencia
        fields = '__all__'


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Equipo
        fields = '__all__'


class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Tarea
        fields = '__all__'

class DiafestivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Tarea
        fields = '__all__'


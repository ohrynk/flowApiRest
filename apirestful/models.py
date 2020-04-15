from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre          = models.CharField(max_length=50)
    sigla           = models.CharField(max_length=2)


class Provincia(models.Model):
    nombre          = models.CharField(max_length=100)
    sigla           = models.CharField(max_length=3)
    pais            = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

class Ciudad(models.Model):
    nombre          = models.CharField(max_length=50)
    sigla           = models.CharField(max_length=2)
    provincia       = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True)

class Idioma(models.Model):
    nombre         =models.CharField(max_length=50)
    sigla          =models.CharField(max_length=2)

class Moneda(models.Model):
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

class Tipodocumento(models.Model):
    nombre      = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)


class Empresa(models.Model):
    nombre       = models.CharField(max_length=100)
    dominio      = models.CharField(max_length=150, null=True, blank=True)
    formatofecha = models.CharField(max_length=2)
    idioma       = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    moneda       = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    razonsocial  = models.CharField(max_length=100)
    cuit         = models.CharField(max_length=30, null=True, blank=True)
    direccion1   = models.CharField(max_length=100)
    direccion2   = models.CharField(max_length=100, null=True, blank=True)
    ciudad       = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)


class Oficina(models.Model):
    nombre          = models.CharField(max_length=100)
    descripcion     = models.CharField(max_length=255)
    direccion       = models.CharField(max_length=255)
    ciudad          = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    empresa         = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)

# Create your models here.
class Empleado(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('V', 'Variado'),
    )
    nombre           = models.CharField(max_length=50)
    apellido         = models.CharField(max_length=50)
    email            = models.CharField(max_length=100, verbose_name='Email')
    reporta          = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    oficina          = models.ForeignKey(Oficina, on_delete=models.CASCADE, null=True)
    nrodocumento     = models.CharField(max_length=30, null=True, blank=True, verbose_name='Nro. Documento')
    tipodocumento    = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Tipo Documento')
    cbu              = models.CharField(max_length=21, blank=True, null=True)
    fechanacimiento  = models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento')
    genero           = models.CharField(max_length=1,choices=GENERO)
    nacionalidad     = models.ForeignKey(Pais,  on_delete=models.CASCADE, null=True)
    telefono         = models.CharField(max_length=30, null=True, blank=True)
    direccion        = models.CharField(max_length=75, blank=True, null=True, verbose_name='Direccion')
    ciudad           = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True,  verbose_name='Ciudad')
    codigopostal     = models.CharField(max_length=20, blank=True, verbose_name='Codigo Postal')


class TipoAusencia(models.Model):
    nombre              = models.CharField(max_length=50)
    descripcion         = models.CharField(max_length=100)
    restavacaciones     = models.BooleanField()
    requiereaprovacion  = models.BooleanField()
    permitedocadjunto   = models.BooleanField()
    ausencialaborable   = models.BooleanField()


class Ausencia(models.Model):
    TIEMPO = (
        ('M', 'Medio Dia'),
        ('E', 'Dia Entero'),
        ('V', 'Varios Dias'),
    )
    TIEMPO_DETALLE = (
        ('1', 'Primer Mitad'),
        ('2', 'Segunda Mitad')
    )
    empleado        = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True,  verbose_name='Empleado')
    tipo            = models.ForeignKey(TipoAusencia, on_delete=models.CASCADE, null=True, verbose_name='Tipo de Ausencia')
    tiempo          = models.CharField(max_length=1, choices=TIEMPO)
    mediodia = models.CharField(max_length=1, choices=TIEMPO_DETALLE)
    fechadesde      = models.DateField(null=True)
    fechahasta      = models.DateField(null=True, blank=True)

class Equipo(models.Model):
    nombre         = models.CharField(max_length=50)
    lider          = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    oficina        = models.ForeignKey(Oficina, on_delete=models.CASCADE,null=True)

class Evento(models.Model):
    organizadopor   = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    oficina         = models.ForeignKey(Oficina, on_delete=models.CASCADE, null=True)
    nombre          = models.CharField(max_length=50)
    descripcion     = models.CharField(max_length=100, null=True, blank=True)
    fecha           = models.DateField()
    hora            = models.TimeField()
    lugar           = models.CharField(max_length=100)

class Tarea(models.Model):
    nombre          = models.CharField(max_length=50)
    descripcion     = models.CharField(max_length=100, null=True, blank=True)
    asignara        = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    fecha           = models.DateField()


class Diafestivo(models.Model):
    oficina         = models.ForeignKey(Oficina, on_delete=models.CASCADE, null=True)
    fecha           = models.DateField()
    nombre          = models.CharField(max_length=50)
    descripcion     = models.CharField(max_length=100, null=True, blank=True)

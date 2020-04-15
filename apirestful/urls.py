from django.urls import include, path
from rest_framework import routers
from . import apiviews
from . import views
from rest_framework.authtoken import views as views_token

router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)
router.register(r'paises', apiviews.PaisViewSet)
router.register(r'provincias', apiviews.ProvinciaViewSet)
router.register(r'ciudades', apiviews.CiudadViewSet)
router.register(r'idiomas', apiviews.IdiomaViewSet)
router.register(r'monedas', apiviews.MonedaViewSet)
router.register(r'tipodocumentos', apiviews.TipodocumentoViewSet)
router.register(r'empresas', apiviews.EmpresaViewSet)
router.register(r'tipoausencias', apiviews.TipoAusenciaViewSet)
router.register(r'ausencias', apiviews.AusenciaViewSet)
router.register(r'equipos', apiviews.EquipoViewSet)
router.register(r'empleados', apiviews.EmpleadoViewSet)
router.register(r'tareas', apiviews.TareaViewSet)
router.register(r'diasfestivos', apiviews.DiafestivoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views_token.obtain_auth_token)
]
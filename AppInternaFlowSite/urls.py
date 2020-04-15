from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('v1/', include('apirestful.urls')),
    path('', admin.site.urls),
    path('polls/', include('polls.urls')),

]

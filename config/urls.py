from django.contrib import admin
from django.urls import path, include
from projetoDjangoApi.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuarios/download', exportar_dados_xlsx)
]

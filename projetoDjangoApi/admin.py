from django.contrib import admin
from projetoDjangoApi.models import Usuario

class Usuarios(admin.ModelAdmin):
  list_display = ('id', 'nome', 'data_nascimento')
  list_display_links = ('id', 'nome')
  search_fields = ('nome',)

admin.site.register(Usuario, Usuarios)



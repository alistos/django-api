from rest_framework import serializers
from projetoDjangoApi.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ['id', 'nome', 'senha', 'data_nascimento']
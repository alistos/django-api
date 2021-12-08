from rest_framework import viewsets
from django.shortcuts import render
from projetoDjangoApi.models import Usuario
import pandas as pd
from projetoDjangoApi.serializer import UsuarioSerializer
from django.http import JsonResponse
import datetime
from rest_framework.decorators import action

class UsuariosViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

#Metódo de exportação dos dados do DB para um arquivo xlsx
def exportar_dados_xlsx(request):
  objetos = Usuario.objects.all()
  data = []

  for obj in objetos:
    data.append({
      "nome" : obj.nome,
      "senha" : obj.senha,
      "data_nascimento" : obj.data_nascimento.strftime('%d/%m/%Y')
    })
  pd.DataFrame(data).to_excel('saida.xlsx')
  return JsonResponse({
    'status': 200
  })
from django.db import models
from django.utils.crypto import get_random_string

class Usuario(models.Model):
  nome = models.CharField(max_length=30, blank=False)
  senha = models.CharField(max_length=20, blank=True)
  data_nascimento = models.DateField(blank=False)

  def __str__(self):
      return self.nome

  #Metodo utilizado para salvar uma senha aleatória caso uma não seja dada no cadastro
  def save(self, *args, **kwargs):
    if self.senha == "":
      self.senha = get_random_string(length=20)
    super(Usuario, self).save(*args, **kwargs)
  

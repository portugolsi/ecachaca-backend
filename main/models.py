from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    cpf = models.CharField(max_length=11,blank=True,null=True)
    def __str__(self) -> str:
        return self.username
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Usuários"

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuario.username
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Avaliações"

class Produto(models.Model):
    nome = models.CharField(max_length=150,help_text="Nome da Cachaça")
    Foto = models.ImageField(upload_to='ImagensCachaca',blank=True)
    

#Foto --
#Produtor
#Categoria
#Descrição --
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(max_length=11,unique=True,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.usuario.username
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Avaliações"

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='FotosProdutores',null=True,blank=True)
    contato = models.CharField(max_length=11)
    def __str__(self) -> str:
        return self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Produtores"


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Categorias"

class Produto(models.Model):
    nome = models.CharField(max_length=150,help_text="Nome da Cachaça")
    foto = models.ImageField(upload_to='ImagensCachaca',blank=True,null=True)
    produtor = models.ForeignKey(Produtor,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descricao = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Produtos"

class QtdCliques(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    qtd =  models.IntegerField(blank=True,null=True)
    
    
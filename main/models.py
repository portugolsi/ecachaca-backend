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

class QtdCliques(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    qtd =  models.IntegerField(blank=True,null=True)
    
    


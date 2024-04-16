from django.contrib import admin
from .models import Produto,Produtor,QtdCliques,Avaliacao,Categoria

admin.site.register(Produtor)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(QtdCliques)
admin.site.register(Avaliacao)
    
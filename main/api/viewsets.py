from rest_framework import viewsets
from main.api.serializers import ProdutoSerializer,AvaliacaoSerializer,CategoriaSerializer,ProdutorSerializer,QtdCliquesSerializer
from main.models import Produto,Avaliacao,Produtor,QtdCliques,Categoria

class ProdutoViewset(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

class AvaliacaoViewset(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()

class CategoriaViewset(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProdutorViewset(viewsets.ModelViewSet):
    serializer_class = ProdutorSerializer
    queryset = Produtor.objects.all()

class QtdCliquesViewset(viewsets.ModelViewSet):
    serializer_class = QtdCliquesSerializer
    queryset = QtdCliques.objects.all()
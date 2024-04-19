from rest_framework import viewsets
from main.api.serializers import ProdutoSerializer,AvaliacaoSerializer,CategoriaSerializer,ProdutorSerializer,QtdCliquesSerializer
from main.models import Produto,Avaliacao,Produtor,QtdCliques,Categoria

class ProdutoViewset(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        # Verifique se o parâmetro 'expand' está presente na solicitação
        expand = self.request.query_params.get('expand')

        if expand:
            # Divida o parâmetro 'expand' em uma lista de campos a serem expandidos
            fields_to_expand = expand.split(',')

            # Verifique se os campos a serem expandidos são campos relacionados em Produto
            allowed_fields = ['produtor', 'categoria']
            fields_to_expand = [field for field in fields_to_expand if field in allowed_fields]

            # Expanda os campos relacionados no queryset usando select_related ou prefetch_related
            for field in fields_to_expand:
                queryset = queryset.select_related(field)

        return queryset

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
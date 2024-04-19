from rest_framework import serializers
from main.models import Produto, Produtor, Avaliacao,QtdCliques,Categoria





class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class QtdCliquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QtdCliques
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    produtor = ProdutorSerializer()  # Use o serializer de Produtor para o campo produtor
    categoria = CategoriaSerializer()  # Use o serializer de Categoria para o campo categoria

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'foto', 'descricao', 'produtor', 'categoria']
from rest_framework import serializers
from main.models import Produto, Produtor, Avaliacao,QtdCliques,Categoria


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

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

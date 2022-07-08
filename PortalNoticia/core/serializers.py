from .models import Categoria, Noticia
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(
        read_only=True, source="categoria.nombre")
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source="categoria")

    class Meta:
        model = Noticia
        fields = '__all__'


from .models import *

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail',
        lookup_field = 'slug'
    )
    class Meta:
        model = Category
        fields = [
            'id',
            'products',
            'first',
            'second',
            'slug',
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    category = CategorySerializer()

    tags = serializers.PrimaryKeyRelatedField(
        queryset=TaggedProduct.objects.all(),
        many=True,
        )

    class Meta:
        model = Product
        fields = (
            'name',
            'img',
            'description',
            'price',
            'category',
            'like',
            'comments',
            'slug',
            'tags',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggableManager
        fields= '__all__'
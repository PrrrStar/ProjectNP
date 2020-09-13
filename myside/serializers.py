
from .models import Category
from .models import Product
from rest_framework import serializers


class ProductCategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name','category','brand','img','description','price','stock','available_display','slug','created_at','modified_at',)
        
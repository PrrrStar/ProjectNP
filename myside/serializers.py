
from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedModelSerializer(
        many = True
        read_only= True
        view_name = 'product_detail'
    )
    class Meta:
        model = Category
        field = ['url','id','name','slug']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','category','brand','img','description','price','stock','available_display','slug','created_at','modified_at',]
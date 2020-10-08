from rest_framework import serializers
from .models import *
from myside.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
        'title',
        'content',
        'board',
        'author',
        'hits',
        'recommends',
        'derecommends',
        'products'
        )

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

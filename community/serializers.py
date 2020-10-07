from rest_framework import serializers
from .models import *


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
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
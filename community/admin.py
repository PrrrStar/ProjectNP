from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','author','hits','created_at')

@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display=('id',)


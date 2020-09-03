from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(Post_comment)
class PostAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Post_recomment)
class PostAdmin(admin.ModelAdmin):
    list_display=('content',)
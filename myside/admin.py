from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','first','second','slug']
    prepopulated_fields = {'slug':('second',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','img','price','tags','available_display','created_at','modified_at')
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ('like',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(ProductTag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_fields = {'slug':('name',)}


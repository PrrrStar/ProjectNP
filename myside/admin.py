from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first','second' )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Recomment)
class RecommentAdmin(admin.ModelAdmin):
    list_display=('content',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('name','img')


#@admin.register(Product_has_brand)
#class Product_has_brandAdmin(admin.ModelAdmin):
#    list_display=()


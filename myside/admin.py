from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first','second' )

class CommentAdmin(admin.ModelAdmin):
    list_display=('content',)
class RecommentAdmin(admin.ModelAdmin):
    list_display=('content',)

class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)

class Product_has_brandAdmin(admin.ModelAdmin):
    list_display=()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Recomment, RecommentAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product_has_brand, Product_has_brandAdmin)
